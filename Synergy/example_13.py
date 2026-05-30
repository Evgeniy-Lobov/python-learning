Names = ['Аня', 'Борис', 'Вера']
scores = [85, 90, 78]
print("Имена студентов и их оценки:")
for zipped_tuple in zip(Names, scores):
    print(zipped_tuple)