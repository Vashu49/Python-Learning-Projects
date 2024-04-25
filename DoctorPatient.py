#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Patient:
    def __init__(self, name):
        self.name = name

class Doctor:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        if len(self.patients) < 16:
            self.patients.append(patient)
            print(f"{patient.name} added to {self.name}'s schedule.")
        else:
            print(f"Sorry, {self.name}'s schedule is full for today.")

class Scheduler:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_patient(self, patient):
        scheduled = False
        for doctor in self.doctors:
            if len(doctor.patients) < 16:
                doctor.add_patient(patient)
                scheduled = True
                break
        if not scheduled:
            print("All doctors' schedules are full for today.")

def main():
    # Creating doctors
    doctor1 = Doctor("Dr. Smith")
    doctor2 = Doctor("Dr. Johnson")

    # Adding doctors to scheduler
    scheduler = Scheduler()
    scheduler.add_doctor(doctor1)
    scheduler.add_doctor(doctor2)

    # Creating patients
    patient1 = Patient("Ram")
    patient2 = Patient("Laxman")
    patient3 = Patient("Bharat")
    patient4 = Patient("Shatrughana")

    # Scheduling patients
    scheduler.schedule_patient(patient1)
    scheduler.schedule_patient(patient2)
    scheduler.schedule_patient(patient3)
    scheduler.schedule_patient(patient4)

if __name__ == "__main__":
    main()


# In[ ]:




