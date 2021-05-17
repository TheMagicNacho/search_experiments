#!/usr/bin/python3
# Embeded from Melzi_Win_V2.0
## IMPORT THE LIBRARY
import imp
import re
import random
import json

imp.load_dynamic('fusionscript', r'C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll')
## TODO: FOR MAC USE-  /Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so



if __name__ == "__main__":
	# # INITIALIZE THE OBJECTS
	projectManager = resolve.GetProjectManager()
	project = projectManager.GetCurrentProject()
	mediaPool = project.GetMediaPool()
	currentFolder = mediaPool.GetCurrentFolder()
	clips = currentFolder.GetClipList()  # Uses clips from the currently open folder (bin)

	# # CHECK FOR TIMELINE. IF NO TIMELINE, CREATE ONE.
	timeline_check = project.GetTimelineCount()
	if timeline_check < 1:
		timelineName = "Timeline ID-" + str(random.randint(1000, 2000))
		timeline = mediaPool.CreateEmptyTimeline(timelineName)
		print("ACTION: Created" + timelineName)
		if not timeline:
			print("NOTICE: Unable to create timeline. Please manually create timeline.")
	else:
		print("NOTICE: Using current active timeline.")

	# # OPEN SCRIPT FILE
	c = open('melzi_config.json')
	config = json.load(c)
	script_path = config[0]['screenplay_path']
	method = config[0]['config_method']
	print('config method')
	print(method)
	# print(script_path)
	# script_path = r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp\dev\script.txt"
	c.close()


	script_data = []
	pat = re.compile(r'[^a-zA-Z ]+')
	str = open(script_path, 'r')
	lst = str.read()
	out = re.sub(pat, ' ', lst).lower()
	script_data = out.split()
	str.close()
	print(script_data)

	# # LOOP LOGIC 4
	clump = []

	for i in range(len(script_data)):  # Read first and next word in script
		print("SEARCHING FOR WORD")
		print(script_data[i])
		print("---")
		for j in clips:  # Loop through all clips in bin
			# Create a list of all keywords in a single clip
			meta_raw = j.GetMetadata('Keywords')
			meta_out = re.sub(pat, ' ', meta_raw).lower()
			meta_data = meta_out.split()
			for k in range(len(meta_data)):  # loop through all keywords in list
				# print("script data" + script_data[i])
				# print("meta data" + meta_data[k])
				if script_data[i] == meta_data[k]:  # Match clip to keyword

					clump.append(j)
		# # Clump is the list of clips that all have the same keywords.
		# # Clump is a python object interprated by Resolve.
		# print(type(clump))

		clump_len = len(clump) - 1
		print("clump Length")
		print(clump_len)
		if clump_len >= 1:
			clump_index = random.randint(int(0), int(clump_len))
			print("Chosen Index")
			print(clump_index)
			chosen = clump[clump_index]
			subClip = {
				'mediaPoolItem': chosen,
			}
			if not mediaPool.AppendToTimeline([subClip]):  # add the matched clip to the timeline
				clump *= 0
				continue
			print('ACTION:  Multiple clips for keyword. Randomly selected clip added.')
			print("==============")
			clump *= 0

		elif clump_len == int(0):
			subClip = {
				'mediaPoolItem': clump[0],
			}
			if mediaPool.AppendToTimeline([subClip]):  # add the matched clip to the timeline
				print('ACTION: Single clip available for keyword. Added to timeline.')
				print("==============")
				clump *= 0
				continue


		else:
			print("NOTICE: Nothing to add.")
			print("==============")
			clump *= 0
			continue