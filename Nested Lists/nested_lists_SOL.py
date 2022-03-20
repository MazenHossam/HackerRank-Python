if __name__ == '__main__':
    all_scores=[]
    student_data=[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_data.append([name,score])
        all_scores.append(score)
    
    all_scores= list(dict.fromkeys(all_scores))
    all_scores.sort()
    student_data.sort()
    
    min=all_scores[1]
    for i in range(len(student_data)):
        if student_data[i][1] == min:
            print(student_data[i][0])
