"""
Basic Report Card Printer
A simple Python program to create and print student report cards
"""

def print_report_card():
    """Main function to create and display a report card"""
    
    print("=" * 60)
    print("                   REPORT CARD PRINTER")
    print("=" * 60)
    print()
    
    # Get student information
    student_name = input("Enter Student Name: ")
    roll_number = input("Enter Roll Number: ")
    class_name = input("Enter Class (e.g., 10-A, 12-B): ")
    
    print()
    print("-" * 60)
    
    # Get number of subjects
    num_subjects = int(input("Enter number of subjects: "))
    
    # Dictionary to store subject marks
    subjects = {}
    total_marks = 0
    
    # Get marks for each subject
    print("\nEnter marks for each subject (out of 100):")
    for i in range(num_subjects):
        subject_name = input(f"Subject {i+1} name: ")
        marks = float(input(f"Marks in {subject_name}: "))
        subjects[subject_name] = marks
        total_marks += marks
    
    print()
    
    # Calculate average and percentage
    average_marks = total_marks / num_subjects
    percentage = (total_marks / (num_subjects * 100)) * 100
    
    # Determine grade based on percentage
    if percentage >= 90:
        grade = 'A+'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 50:
        grade = 'D'
    else:
        grade = 'F'
    
    # Print the report card
    print("=" * 60)
    print("                    REPORT CARD")
    print("=" * 60)
    print()
    print(f"Name:           {student_name}")
    print(f"Roll Number:    {roll_number}")
    print(f"Class:          {class_name}")
    print()
    print("-" * 60)
    print("SUBJECT WISE PERFORMANCE")
    print("-" * 60)
    print(f"{'Subject':<30} {'Marks':<15} {'Status'}")
    print("-" * 60)
    
    # Display marks for each subject
    for subject, marks in subjects.items():
        status = "Pass" if marks >= 35 else "Fail"
        print(f"{subject:<30} {marks:<15} {status}")
    
    print("-" * 60)
    print()
    print("SUMMARY")
    print("-" * 60)
    print(f"Total Marks:        {total_marks} / {num_subjects * 100}")
    print(f"Average Marks:      {average_marks:.2f}")
    print(f"Percentage:         {percentage:.2f}%")
    print(f"Grade:              {grade}")
    print("-" * 60)
    
    # Remarks based on grade
    if grade in ['A+', 'A']:
        remarks = "Excellent! Keep up the outstanding performance."
    elif grade == 'B':
        remarks = "Good! Continue to improve and maintain focus."
    elif grade == 'C':
        remarks = "Average. Work harder to improve your grades."
    elif grade == 'D':
        remarks = "Poor. Seek additional help and guidance."
    else:
        remarks = "Fail. Please consult your teacher immediately."
    
    print(f"Remarks:            {remarks}")
    print()
    print("=" * 60)
    print("            Thank you for using Report Card Printer")
    print("=" * 60)


def main():
    """Main function to run the program"""
    while True:
        print_report_card()
        
        # Ask if user wants to print another report card
        another = input("\nDo you want to print another report card? (yes/no): ").lower()
        if another != 'yes' and another != 'y':
            print("\nThank you! Goodbye!")
            break
        print("\n")


if __name__ == "__main__":
    main()
