from typing import Set, List, Optional

class Teacher:
    def __init__(self, first_name: str, last_name: str, age: int, email: str, can_teach_subjects: Set[str]):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects: Set[str] = set()

def create_schedule(subjects: Set[str], teachers: List[Teacher]) -> Optional[List[Teacher]]:
    # Create a copy of subjects to track uncovered subjects
    uncovered_subjects = subjects.copy()
    selected_teachers = []
    
    while uncovered_subjects:
        # Find the teacher who can teach the most remaining subjects
        best_teacher = None
        max_subjects_can_teach = 0
        
        for teacher in teachers:
            # Skip teachers who are already selected
            if teacher in selected_teachers:
                continue
                
            # Calculate how many uncovered subjects this teacher can teach
            subjects_can_teach = len(teacher.can_teach_subjects.intersection(uncovered_subjects))
            
            # Update best teacher if this one can teach more subjects or is younger
            if subjects_can_teach > 0 and (
                subjects_can_teach > max_subjects_can_teach or 
                (subjects_can_teach == max_subjects_can_teach and 
                 best_teacher and teacher.age < best_teacher.age)
            ):
                best_teacher = teacher
                max_subjects_can_teach = subjects_can_teach
        
        # If no teacher can teach remaining subjects, return None
        if not best_teacher:
            return None
            
        # Assign subjects to the selected teacher
        best_teacher.assigned_subjects = best_teacher.can_teach_subjects.intersection(uncovered_subjects)
        selected_teachers.append(best_teacher)
        
        # Remove covered subjects from uncovered set
        uncovered_subjects -= best_teacher.assigned_subjects
    
    return selected_teachers

if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    
    # Створення списку викладачів
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", 
                {'Математика', 'Фізика'}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", 
                {'Хімія'}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", 
                {'Інформатика', 'Математика'}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", 
                {'Біологія', 'Хімія'}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", 
                {'Фізика', 'Інформатика'}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", 
                {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.") 