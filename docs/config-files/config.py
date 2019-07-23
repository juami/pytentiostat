# Reference:

# brew install libyaml
# sudo python -m easy_install pyyaml
# http://net-informations.com/python/file/open.htm
# https://www.basinc.com/manuals/EC_epsilon/Techniques/ChronoI/ca

import yaml

def main():
    config_file = open("config.yml","r") # open a file

    loaded = yaml.load(config_file)
    print("Name of the file: ", config_file.name)
    print("Opening mode: ", config_file.mode)
    
# need to implement input range error message:

    for key, value in loaded.items():
        for key2, value2 in value.items():
            print("{}:{} \n - parameters:{}".format(key, key2, value2))
    

if __name__ == "__main__":
    main()
