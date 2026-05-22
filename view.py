import tkinter as tk
from tkinter import messagebox

class MainView:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Gestión de Tensiones - E1")
        self.root.geometry("1000x720")

        self.create_patient_section()
        self.create_tension_section()
        self.create_results_section()

    def create_patient_section(self):
        frame = tk.LabelFrame(self.root, text="Pacientes")
        frame.pack(fill="x", padx=10, pady=5)

        tk.Label(frame, text="Nombre").grid(row=0, column=0)
        tk.Label(frame, text="Apellidos").grid(row=0, column=2)
        tk.Label(frame, text="Género").grid(row=1, column=0)
        tk.Label(frame, text="Fecha nacimiento").grid(row=1, column=2)

        self.name_entry = tk.Entry(frame)
        self.surname_entry = tk.Entry(frame)
        self.gender_entry = tk.Entry(frame)
        self.birth_entry = tk.Entry(frame)

        self.name_entry.grid(row=0, column=1)
        self.surname_entry.grid(row=0, column=3)
        self.gender_entry.grid(row=1, column=1)
        self.birth_entry.grid(row=1, column=3)

        tk.Button(frame, text="Añadir paciente", command=self.add_patient).grid(row=2, column=0, pady=5)
        tk.Button(frame, text="Listar pacientes", command=self.list_patients).grid(row=2, column=1, pady=5)
        tk.Button(frame, text="Actualizar paciente", command=self.update_patient).grid(row=2, column=2, pady=5)
        tk.Button(frame, text="Eliminar paciente por ID", command=self.delete_patient).grid(row=2, column=3, pady=5)

        tk.Label(frame, text="ID paciente").grid(row=3, column=0)
        self.patient_id_entry = tk.Entry(frame, width=60)
        self.patient_id_entry.grid(row=3, column=1, columnspan=3)

    def create_tension_section(self):
        frame = tk.LabelFrame(self.root, text="Tensiones")
        frame.pack(fill="x", padx=10, pady=5)

        labels = [
            "Sistólica", "Diastólica", "Método", "Sitio cuerpo",
            "Brazalete", "Dispositivo", "Estado", "Fecha", "Descripción"
        ]

        self.tension_entries = {}

        for i, label in enumerate(labels):
            tk.Label(frame, text=label).grid(row=i // 2, column=(i % 2) * 2)
            entry = tk.Entry(frame)
            entry.grid(row=i // 2, column=(i % 2) * 2 + 1)
            self.tension_entries[label] = entry

        tk.Label(frame, text="ID tensión").grid(row=5, column=0)
        self.tension_id_entry = tk.Entry(frame, width=60)
        self.tension_id_entry.grid(row=5, column=1, columnspan=3)

        tk.Button(frame, text="Añadir tensión", command=self.add_tension).grid(row=6, column=0, pady=5)
        tk.Button(frame, text="Listar todas tensiones", command=self.list_all_tensions).grid(row=6, column=1, pady=5)
        tk.Button(frame, text="Ver tensiones paciente", command=self.list_tensions).grid(row=6, column=2, pady=5)
        tk.Button(frame, text="Actualizar tensión", command=self.update_tension).grid(row=6, column=3, pady=5)
        tk.Button(frame, text="Eliminar tensión por ID", command=self.delete_tension).grid(row=7, column=0, pady=5)
        tk.Button(frame, text="Media tensiones", command=self.average_tension).grid(row=7, column=1, pady=5)
        tk.Button(frame, text="Última tensión", command=self.last_tension).grid(row=7, column=2, pady=5)

    def create_results_section(self):
        frame = tk.LabelFrame(self.root, text="Resultados")
        frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.results = tk.Text(frame, height=18)
        self.results.pack(fill="both", expand=True)

    def add_patient(self):
        try:
            self.controller.add_patient(
                self.name_entry.get(),
                self.surname_entry.get(),
                self.gender_entry.get(),
                self.birth_entry.get()
            )
            messagebox.showinfo("Correcto", "Paciente añadido")
            self.list_patients()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def list_patients(self):
        self.results.delete("1.0", tk.END)
        patients = self.controller.get_patients()

        for p in patients:
            self.results.insert(
                tk.END,
                f"ID: {p['_id']} | {p['name']} {p['surname']} | Género: {p['gender']} | Nacimiento: {p['birth_date']}\n"
            )

    def update_patient(self):
        try:
            self.controller.update_patient(
                self.patient_id_entry.get(),
                self.name_entry.get(),
                self.surname_entry.get(),
                self.gender_entry.get(),
                self.birth_entry.get()
            )
            messagebox.showinfo("Correcto", "Paciente actualizado")
            self.list_patients()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_patient(self):
        try:
            self.controller.delete_patient(self.patient_id_entry.get())
            messagebox.showinfo("Correcto", "Paciente eliminado")
            self.list_patients()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def get_tension_form_data(self):
        return {
            "patient_id": self.patient_id_entry.get(),
            "systolic": self.tension_entries["Sistólica"].get(),
            "diastolic": self.tension_entries["Diastólica"].get(),
            "method": self.tension_entries["Método"].get(),
            "body_site": self.tension_entries["Sitio cuerpo"].get(),
            "cuff_size": self.tension_entries["Brazalete"].get(),
            "device": self.tension_entries["Dispositivo"].get(),
            "state": self.tension_entries["Estado"].get(),
            "date": self.tension_entries["Fecha"].get(),
            "description": self.tension_entries["Descripción"].get()
        }

    def add_tension(self):
        try:
            self.controller.add_tension(self.get_tension_form_data())
            messagebox.showinfo("Correcto", "Tensión añadida")
            self.list_all_tensions()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def list_all_tensions(self):
        self.results.delete("1.0", tk.END)
        tensions = self.controller.get_all_tensions()

        for t in tensions:
            self.results.insert(
                tk.END,
                f"ID: {t['_id']} | Paciente: {t['patient_id']} | Sistólica: {t['systolic']} | Diastólica: {t['diastolic']} | Fecha: {t['date']} | En rango: {t['in_range']} | {t['description']}\n"
            )

    def list_tensions(self):
        self.results.delete("1.0", tk.END)
        tensions = self.controller.get_tensions_by_patient(self.patient_id_entry.get())

        for t in tensions:
            self.results.insert(
                tk.END,
                f"ID: {t['_id']} | Sistólica: {t['systolic']} | Diastólica: {t['diastolic']} | Fecha: {t['date']} | En rango: {t['in_range']} | {t['description']}\n"
            )

    def update_tension(self):
        try:
            self.controller.update_tension(
                self.tension_id_entry.get(),
                self.get_tension_form_data()
            )
            messagebox.showinfo("Correcto", "Tensión actualizada")
            self.list_all_tensions()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_tension(self):
        try:
            self.controller.delete_tension(self.tension_id_entry.get())
            messagebox.showinfo("Correcto", "Tensión eliminada")
            self.list_all_tensions()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def average_tension(self):
        result = self.controller.get_average(self.patient_id_entry.get())

        if result is None:
            messagebox.showinfo("Sin datos", "No hay tensiones para este paciente")
        else:
            self.results.delete("1.0", tk.END)
            self.results.insert(tk.END, f"Media sistólica: {result[0]}\nMedia diastólica: {result[1]}")

    def last_tension(self):
        result = self.controller.get_last_tension(self.patient_id_entry.get())

        if result is None:
            messagebox.showinfo("Sin datos", "No hay tensiones para este paciente")
        else:
            self.results.delete("1.0", tk.END)
            self.results.insert(
                tk.END,
                f"Última toma:\nSistólica: {result['systolic']}\nDiastólica: {result['diastolic']}\nFecha: {result['date']}\nDescripción: {result['description']}\nEn rango: {result['in_range']}"
            )

    def run(self):
        self.root.mainloop()