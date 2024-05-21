import matplotlib.pyplot as plt

# Example data
test_instances = [1, 2, 3, 4, 5]
pregnancies = [2, 3, 1, 4, 2]
glucose = [90, 180, 110, 150, 200]
blood_pressure = [70, 85, 80, 90, 95]
skin_thickness = [20, 35, 25, 30, 40]
insulin = [80, 130, 100, 120, 150]
bmi = [22.0, 28.5, 24.0, 27.0, 30.0]
diabetes_pedigree = [0.5, 0.8, 0.6, 0.75, 0.9]
age = [25, 35, 30, 40, 45]
# Dummy diabetes prediction (1 if diabetes, 0 if not)
diabetes_prediction = [0, 1, 0, 1, 1]

# Create the plot
plt.figure(figsize=(14, 8))

# Plot parameters
plt.plot(test_instances, pregnancies, label='Pregnancies', marker='o')
plt.plot(test_instances, glucose, label='Glucose', marker='o')
plt.plot(test_instances, blood_pressure, label='Blood Pressure', marker='o')
plt.plot(test_instances, skin_thickness, label='Skin Thickness', marker='o')
plt.plot(test_instances, insulin, label='Insulin', marker='o')
plt.plot(test_instances, bmi, label='BMI', marker='o')
plt.plot(test_instances, diabetes_pedigree,
         label='Diabetes Pedigree Function', marker='o')
plt.plot(test_instances, age, label='Age', marker='o')

# Highlight points where diabetes is predicted
for i in range(len(test_instances)):
    if diabetes_prediction[i] == 1:
        plt.scatter(test_instances[i], pregnancies[i],
                    color='red', s=100, zorder=5)
        plt.scatter(test_instances[i], glucose[i],
                    color='red', s=100, zorder=5)
        plt.scatter(test_instances[i], blood_pressure[i],
                    color='red', s=100, zorder=5)
        plt.scatter(test_instances[i], skin_thickness[i],
                    color='red', s=100, zorder=5)
        plt.scatter(test_instances[i], insulin[i],
                    color='red', s=100, zorder=5)
        plt.scatter(test_instances[i], bmi[i], color='red', s=100, zorder=5)
        plt.scatter(
            test_instances[i], diabetes_pedigree[i], color='red', s=100, zorder=5)
        plt.scatter(test_instances[i], age[i], color='red', s=100, zorder=5)
        plt.annotate('Diabetes', (test_instances[i], glucose[i]), textcoords="offset points", xytext=(
            0, 10), ha='center', color='red')

plt.xlabel('Test Instance')
plt.ylabel('Value')
plt.title('User Tracking Over Time with Diabetes Prediction')
plt.legend()
plt.grid(True)
plt.show()
