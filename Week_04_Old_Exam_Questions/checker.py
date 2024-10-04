# SOLUTION CHECKER
def check_solution(solutions):
    global Gesamtpunkte
    Gesamtpunkte = 0
    for i in range(1, 8):
        print(test_exercise(solutions[i-1], i))
    return f"{'Bestanden' if Gesamtpunkte >= 20 else 'Durchgefallen'} mit {Gesamtpunkte}/40.0 Punkten"   

def test_exercise(solution, exercise):
    global Gesamtpunkte
    match exercise:
        case 1:
            punkte = 0
            if solution[0] == 5: punkte += 0.5
            if solution[1] == 3: punkte += 0.5
            if solution[2] == 8: punkte += 1.0
            Gesamtpunkte += punkte
            return f"Aufgabe 1: {punkte}/2.0 Punkten"
        case 2:
            punkte = 0
            if solution[0] == "s": punkte += 1.0
            if solution[1] == "f": punkte += 1.0
            if solution[2] == "b": punkte += 1.0
            if solution[3] == "i": punkte += 1.0
            if solution[4] == "i": punkte += 1.0
            if solution[5] == "i": punkte += 1.0
            if solution[6] == "s": punkte += 1.0
            Gesamtpunkte += punkte
            return f"Aufgabe 2: {punkte}/7.0 Punkten"
        case 3:
            punkte = 0
            if 4 in solution: punkte += 1.5
            if 6 in solution: punkte += 1.5
            Gesamtpunkte += punkte
            return f"Aufgabe 3: {punkte}/3.0 Punkten"
        case 4:
            punkte = 0
            if 0 in solution: punkte += 1.0
            if 10 in solution: punkte += 1.0
            if len(solution) == 11: punkte += 1.0
            Gesamtpunkte += punkte
            return f"Aufgabe 4: {punkte}/3.0 Punkten"
        case 5:
            punkte = 0
            if solution("As") == False: punkte += 2.0
            if solution("anna") == True: punkte += 2.0
            if (solution("Paliilap") == True): punkte += 2.0
            if (solution('Ein Esel lese nie.') == True): punkte += 4.0
            Gesamtpunkte += punkte
            return f"Aufgabe 5: {punkte}/10.0 Punkten"
        case 6:
            punkte = 0
            if solution(6) == True: punkte += 2.5
            if solution(5) == False: punkte += 2.5
            Gesamtpunkte += punkte
            return f"Aufgabe 6: {punkte}/5.0 Punkten"
        case 7:
            punkte = 0
            student = solution('Student', 'Python', 'Programmieren')
            if student: punkte += 2
            if student.name == "Student": punkte += 2.0
            if student.studiengang == "Python": punkte += 2.0
            if student.hobby == "Programmieren": punkte += 2.0
            if student.__str__() == "Student studiert Python und liebt Programmieren": punkte += 2.0
            Gesamtpunkte += punkte
            return f"Aufgabe 7: {punkte}/10.0 Punkten"
    