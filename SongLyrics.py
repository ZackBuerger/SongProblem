import itertools
import math



#Takes in the set of sentances, the specified sentance that must be included in the sets and the amount of sentances in each combination 
#Computes the best combination of sentances that minimizes the number of words needed to create all of them individually 
def get_best_combination(sentances, specified_sentance, length):
    best_combo = []
    best_val = float('inf')  # Initialize with infinity for comparison
    print(sentances)
    combos = itertools.combinations(sentances, length-1)
    specifcWords = set()
    num_combos = math.comb(len(sentances), length - 1)
    print("the amount of combos is: "+ str(num_combos))
    for word in specific_sentance.split():
            specifcWords.update(word)
    for combo in combos:
        words = set()
        for word in specifcWords:
            words.update(word)
        
        
        for sentance in combo:
            words.update(sentance.split())
        
        if len(words) < best_val:
            best_val = len(words)
            best_combo = combo
            print("New best found :) : " + str(best_val))
            for i, sentance in enumerate(best_combo, 1):
                print(f"{i}. {sentance}")
            print(f"{length}. {specified_sentance}")
    
    return best_combo, best_val

def get_best_combination_greedy(sentances, specified_sentance, length, max_depth = 5):
    pass
    
#Formating the input data into a set of lines from the songs that are being inputted 
#Filters songs that are bellow the minimum_words 
# removes the specific_sentance from the set as this is not necessary for computing the combinations 
def create_sentances_list(file_path, minimum_words, specific_sentance):
    sentances_set = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            if len(words) > minimum_words:
                sentances_set.add(line.strip())
    sentances_set.remove(specific_sentance)
    return list(sentances_set)

file_path = 'C:\\Users\\zacha\\Desktop\\Songs to check\\songs.txt'
specific_sentance = "I'm gonna love you for a long time"
sentances = create_sentances_list(file_path, 3, specific_sentance)

x = 7


best_combo, val = get_best_combination(sentances, specific_sentance, x)
print("Selected sentances:")
for i, sentance in enumerate(best_combo, 1):
    print(f"{i}. {sentance}")

print("\nTotal number of words used:", val)