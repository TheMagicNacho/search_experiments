import re
import Payload
import random

#Define Script Path
script_path = "script.txt"
# clips = {
#     'obj1' : ['coffee', 'chicken', 'taco'], 
#     'obj2' : ['love', 'ache', 'sonic', 'movie', 'chicken'], 
#     'obj3' : ['drink', 'now', 'this', 'cofeetime'], 
#     'obj4' : ['coffeetime', 'morning', 'brown', 'coffee']
#     }

# script_dic = 'coffee'

clips = {
    'obj1' : [],
    'obj2' : [],
    'obj3' : [],
    'obj4' : [],
    'obj6' : [],
    'obj7' : [],
}
clips['obj1'] = Payload.MetaData1()
clips['obj2'] = Payload.MetaData2()
clips['obj3'] = Payload.MetaData3()
clips['obj4'] = Payload.MetaData1()
clips['obj5'] = Payload.MetaData2()
clips['obj6'] = Payload.MetaData3()
clips['obj7'] = Payload.MetaData1()


#Load the Screenplay as a list
script_data = []
def LoadScript(script_path):
    pat = re.compile(r'[^a-zA-Z ]+')
    str = open(script_path, 'r')
    lst = str.read()
    out = re.sub(pat, ' ', lst).lower()
    script_data = out.split()
    str.close()
    return script_data


def Search(clips, search):
    clump = []
    for k, v in clips.items():
        if search in v:
            clump.append(k)
    return clump

def ClumManager(clump):
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
        print(subClip)
       
        ### Uncomment next three lines when in production
        # if not mediaPool.AppendToTimeline([subClip]):  # add the matched clip to the timeline
        #     clump *= 0
        #     continue
        print('ACTION:  Multiple clips for keyword. Randomly selected clip added.')
        print("==============")
        clump *= 0

    elif clump_len == int(0):
        subClip = {
            'mediaPoolItem': clump[0],
        }
        print(subClip)
        print('ACTION: Single clip available for keyword. Added to timeline.')
        print("==============")
        clump *= 0
    

        ### Uncomment next line when in production
        # if mediaPool.AppendToTimeline([subClip]):  # add the matched clip to the timeline
            # print('ACTION: Single clip available for keyword. Added to timeline.')
            # print("==============")
            # clump *= 0
            # continue

    else:
        print("NOTICE: Nothing to add.")
        print("==============")
        clump *= 0

def Prime():
    script_dic = LoadScript(script_path)
    print(script_dic)
    for item in script_dic:
        clump = Search(clips, item)
        ClumManager(clump)

Prime()