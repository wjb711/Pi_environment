import json
import sys
def writejson(file,key,value):

#记录历史，写json文件的方法

    try:

        with open(file,"r") as f:

            load_dict = json.load(f)

    except:

        load_dict={}

#    print(type(load_dict),load_dict)
    #for x in load_dict:
    #    print(x)
    #load_dict=load_dict[0]
    load_dict[key]=value
    print(load_dict)
#    dict0['item1']=str(item1)

#    dict0['item2']=str(item2)

#    dict0['item3']=str(item3)

#    load_dict.append(dict0)

#    with open("config.json","w") as f:



#        json.dump(load_dict,f)

    with open(file, 'w', encoding = 'UTF-8') as f:
        json.dump(load_dict, f, ensure_ascii = False, indent = 2)

def readjson(file,key):
    try:

        with open(file,"r") as f:

            load_dict = json.load(f)

    except:

        load_dict={}

    return load_dict[key]

if __name__=='__main__':
    key=sys.argv[1]
    value=sys.argv[2]
    writejson('config.json',key,value)
#print(readjson('config.json','key2'))
