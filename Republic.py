import argparse
import string
import time 

file_path = "Republic.txt"

def process_file(file_path):
    start_time = time.time()
    count_dict = {character: 0 for character in string.ascii_lowercase}
    '''
    for character in string.ascii_lowercase:
        count_dict[character] = 0
        '''
    with open(file_path) as input_file:
        for line in input_file:
            for character in line.lower():
                try:
                    count_dict[character] += 1
                except KeyError:
                    pass

                ''' 
                if character in count_dict:
                    count_dict[character] += 1
                else:
                    count_dict[character] = 1
                '''
            #print(line)
            #print(type(line))
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.3f} seconds")
    print(count_dict)

if __name__ == "__main__":
    #process_file(file_path)
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")

    args = parser.parse_args()
    #print(args)
    #print(args.filepath)
    process_file(args.filepath)


'''dir()'''