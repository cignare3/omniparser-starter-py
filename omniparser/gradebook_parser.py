
import pandas
import os
import statistics

def calculate_average_grade_from_csv(my_csv_filepath):
    df = pandas.read_csv(my_csv_filepath) 
    #breakpoint()

    #rows = df.to_dict("records")
    #grades = [r["final_grade"] for r in rows]
    #avg_grade = statistics.mean(grades)

    #grades = df["final_grade"].to_list()
    #avg_grade = statistics.mean(grades)
    
    avg_grade = df["final_grade"].mean()

    return avg_grade #90.64
    

if __name__ == "__main__":
    print("PARSING SOME EXAMPLE GRADEBOOK FILES HERE...")

    gradebook_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "gradebook_2019.csv")
    print(gradebook_filepath)
    
    #gradebook_filepath = "C::\Users\tyler\Documents\GitHub\omniparser-starter-py\data\gradebook_2018.csv"
    
    #gradebook_filepath = "data\gradebook_2018.csv"
    #breakpoint()
    avg = calculate_average_grade_from_csv(gradebook_filepath)
    print(avg)