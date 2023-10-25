cosunak_count = int(input())
the_best_shef = ""
the_best_score = 0
for _ in range(1, cosunak_count + 1):
    assessors_counter = 0
    cosunac_score = 0
    chef_name = input()
    while True:
        score = input()
        if score == "Stop":
            print(f"{chef_name} has {cosunac_score} points.")
            break
        score = int(score)
        assessors_counter += 1
        cosunac_score += score
    if the_best_score <= cosunac_score:
        the_best_score = cosunac_score
        the_best_shef = chef_name
        print(f"{chef_name} is the new number 1!")
print(f"{the_best_shef} won competition with {the_best_score} points!")