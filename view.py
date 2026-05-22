import tkinter as tk
from tkinter import messagebox

class MainView:

    def __init__(self, controller):

        self.controller = controller

        self.patient_map = {}
        self.tension_map = {}

        self.root = tk.Tk()
        self.root.title("Gestión de Tensiones")
        self.root.geometry("1100x780")

        self.create_patient_section()
        self.create_tension_section()
        self.create_results_section()

    def create_patient_section(self):

        frame = tk.LabelFrame(self.root, text="Pacientes")
        frame.pack(fill="x", padx=10, pady=5)

        tk.Label(frame, text="Nombre").grid(row=0, column=0)
        tk.Label(frame, text="Apellidos").grid(row=0, column=2)
        tk.Label(frame, text="Género").grid(row=1, column=0)
        tk.Label(frame, text="Nacimiento YYYY-MM-DD").grid(row=1, column=2)

        self.name_entry = tk.Entry(frame)
        self.surname_entry = tk.Entry(frame)

        self.gender_var = tk.StringVar(value="female")

        self.gender_menu = tk.OptionMenu(
            frame,
            self.gender_var,
            "male",
            "female",
            "other",
            "unknown"
        )

        self.birth_entry = tk.Entry(frame)

        self.name_entry.grid(row=0, column=1)
        self.surname_entry.grid(row=0, column=3)
        self.gender_menu.grid(row=1, column=1)
        self.birth_entry.grid(row=1, column=3)

        tk.Button(
            frame,
            text="Crear paciente",
            command=self.add_patient
        ).grid(row=2, column=0, pady=5)

        tk.Button(
            frame,
            text="Listar pacientes",
            command=self.list_patients
        ).grid(row=2, column=1, pady=5)

        tk.Button(
            frame,
            text="Actualizar paciente",
            command=self.update_patient
        ).grid(row=2, column=2, pady=5)

        tk.Button(
            frame,
            text="Eliminar paciente",
            command=self.delete_patient
        ).grid(row=2, column=3, pady=5)

        tk.Label(
            frame,
            text="Paciente seleccionado"
        ).grid(row=3, column=0)

        self.selected_patient = tk.StringVar()

        self.patient_menu = tk.OptionMenu(
            frame,
            self.selected_patient,
            ""
        )

        self.patient_menu.grid(
            row=3,
            column=1,
            columnspan=3,
            sticky="ew"
        )

    def create_tension_section(self):

        frame = tk.LabelFrame(self.root, text="Tensiones")
        frame.pack(fill="x", padx=10, pady=5)

        labels = [
            "Sistólica",
            "Diastólica",
            "Método",
            "Sitio cuerpo",
            "Brazalete",
            "Dispositivo",
            "Fecha YYYY-MM-DD",
            "Descripción"
        ]

        self.tension_entries = {}

        for i, label in enumerate(labels):

            tk.Label(
                frame,
                text=label
            ).grid(row=i // 2, column=(i % 2) * 2)

            entry = tk.Entry(frame)

            entry.grid(
                row=i // 2,
                column=(i % 2) * 2 + 1
            )

            self.tension_entries[label] = entry

        tk.Label(frame, text="Estado").grid(row=4, column=0)

        self.state_var = tk.StringVar(value="final")

        self.state_menu = tk.OptionMenu(
            frame,
            self.state_var,
            "registered",
            "preliminary",
            "final",
            "amended",
            "corrected",
            "cancelled",
            "entered-in-error",
            "unknown"
        )

        self.state_menu.grid(row=4, column=1)

        tk.Label(
            frame,
            text="Tensión seleccionada"
        ).grid(row=5, column=0)

        self.selected_tension = tk.StringVar()

        self.tension_menu = tk.OptionMenu(
            frame,
            self.selected_tension,
            ""
        )

        self.tension_menu.grid(
            row=5,
            column=1,
            columnspan=3,
            sticky="ew"
        )

        tk.Button(
            frame,
            text="Crear tensión",
            command=self.add_tension
        ).grid(row=6, column=0, pady=5)

        tk.Button(
            frame,
            text="Listar tensiones",
            command=self.list_all_tensions
        ).grid(row=6, column=1, pady=5)

        tk.Button(
            frame,
            text="Ver tensiones paciente",
            command=self.list_tensions
        ).grid(row=6, column=2, pady=5)

        tk.Button(
            frame,
            text="Actualizar tensión",
            command=self.update_tension
        ).grid(row=6, column=3, pady=5)

        tk.Button(
            frame,
            text="Eliminar tensión",
            command=self.delete_tension
        ).grid(row=7, column=0, pady=5)

        tk.Button(
            frame,
            text="Media tensiones",
            command=self.average_tension
        ).grid(row=7, column=1, pady=5)

        tk.Button(
            frame,
            text="Última tensión",
            command=self.last_tension
        ).grid(row=7, column=2, pady=5)

    def create_results_section(self):

        frame = tk.LabelFrame(
            self.root,
            text="Resultados"
        )

        frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )

        self.results = tk.Text(frame, height=18)

        self.results.pack(
            fill="both",
            expand=True
        )

    def refresh_patient_menu(self):

        patients = self.controller.get_patients()

        self.patient_map = {}

        menu = self.patient_menu["menu"]

        menu.delete(0, "end")

        for p in patients:

            label = (
                f"{p['name']} "
                f"{p['surname']} | "
                f"{p['gender']} | "
                f"{p['birth_date']}"
            )

            self.patient_map[label] = str(p["_id"])

            menu.add_command(
                label=label,
                command=lambda value=label:
                self.selected_patient.set(value)
            )

        if patients:

            first_label = list(
                self.patient_map.keys()
            )[0]

            self.selected_patient.set(first_label)

    def refresh_tension_menu(self, tensions=None):

        if tensions is None:
            tensions = self.controller.get_all_tensions()

        self.tension_map = {}

        menu = self.tension_menu["menu"]

        menu.delete(0, "end")

        for t in tensions:

            patient_name = self.get_patient_label_by_id(
                t["patient_reference"]
            )

            label = (
                f"{patient_name} | "
                f"{t['systolic']}/{t['diastolic']} | "
                f"{t['date']} | "
                f"{t['state']}"
            )

            self.tension_map[label] = str(t["_id"])

            menu.add_command(
                label=label,
                command=lambda value=label:
                self.selected_tension.set(value)
            )

        if tensions:

            first_label = list(
                self.tension_map.keys()
            )[0]

            self.selected_tension.set(first_label)

    def get_selected_patient_id(self):

        label = self.selected_patient.get()

        return self.patient_map[label]

    def get_selected_tension_id(self):

        label = self.selected_tension.get()

        return self.tension_map[label]

    def get_patient_label_by_id(self, patient_reference):

        for label, stored_id in self.patient_map.items():

            if stored_id == patient_reference:

                return label.split("|")[0].strip()

        return "Paciente"

    def add_patient(self):

        try:

            self.controller.create_patient(
                self.name_entry.get(),
                self.surname_entry.get(),
                self.gender_var.get(),
                self.birth_entry.get()
            )

            messagebox.showinfo(
                "Correcto",
                "Paciente creado"
            )

            self.list_patients()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def list_patients(self):

        self.results.delete("1.0", tk.END)

        patients = self.controller.get_patients()

        self.refresh_patient_menu()

        for p in patients:

            self.results.insert(
                tk.END,
                f"{p['name']} "
                f"{p['surname']} | "
                f"Género: {p['gender']} | "
                f"Nacimiento: {p['birth_date']}\n"
            )

    def update_patient(self):

        try:

            patient_id = self.get_selected_patient_id()

            self.controller.update_patient(
                patient_id,
                self.name_entry.get(),
                self.surname_entry.get(),
                self.gender_var.get(),
                self.birth_entry.get()
            )

            messagebox.showinfo(
                "Correcto",
                "Paciente actualizado"
            )

            self.list_patients()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def delete_patient(self):

        try:

            patient_id = self.get_selected_patient_id()

            self.controller.delete_patient(
                patient_id
            )

            messagebox.showinfo(
                "Correcto",
                "Paciente eliminado"
            )

            self.list_patients()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def get_tension_form_data(self):

        return {

            "patient_reference":
            self.get_selected_patient_id(),

            "systolic":
            self.tension_entries["Sistólica"].get(),

            "diastolic":
            self.tension_entries["Diastólica"].get(),

            "method":
            self.tension_entries["Método"].get(),

            "body_site":
            self.tension_entries["Sitio cuerpo"].get(),

            "cuff_size":
            self.tension_entries["Brazalete"].get(),

            "device":
            self.tension_entries["Dispositivo"].get(),

            "state":
            self.state_var.get(),

            "date":
            self.tension_entries[
                "Fecha YYYY-MM-DD"
            ].get(),

            "description":
            self.tension_entries[
                "Descripción"
            ].get()
        }

    def add_tension(self):

        try:

            self.controller.create_tension(
                self.get_tension_form_data()
            )

            messagebox.showinfo(
                "Correcto",
                "Tensión creada"
            )

            self.list_all_tensions()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def list_all_tensions(self):

        self.results.delete("1.0", tk.END)

        self.refresh_patient_menu()

        tensions = self.controller.get_all_tensions()

        self.refresh_tension_menu(tensions)

        for t in tensions:

            patient_name = self.get_patient_label_by_id(
                t["patient_reference"]
            )

            self.results.insert(
                tk.END,
                f"Paciente: {patient_name} | "
                f"Sistólica: {t['systolic']} | "
                f"Diastólica: {t['diastolic']} | "
                f"Fecha: {t['date']} | "
                f"Estado: {t['state']} | "
                f"En rango: {t['in_range']} | "
                f"{t['description']}\n"
            )

    def list_tensions(self):

        self.results.delete("1.0", tk.END)

        patient_reference = (
            self.get_selected_patient_id()
        )

        tensions = (
            self.controller.get_tensions_by_patient(
                patient_reference
            )
        )

        self.refresh_tension_menu(tensions)

        for t in tensions:

            self.results.insert(
                tk.END,
                f"Sistólica: {t['systolic']} | "
                f"Diastólica: {t['diastolic']} | "
                f"Fecha: {t['date']} | "
                f"Estado: {t['state']} | "
                f"En rango: {t['in_range']} | "
                f"{t['description']}\n"
            )

    def update_tension(self):

        try:

            tension_id = self.get_selected_tension_id()

            self.controller.update_tension(
                tension_id,
                self.get_tension_form_data()
            )

            messagebox.showinfo(
                "Correcto",
                "Tensión actualizada"
            )

            self.list_all_tensions()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def delete_tension(self):

        try:

            tension_id = self.get_selected_tension_id()

            self.controller.delete_tension(
                tension_id
            )

            messagebox.showinfo(
                "Correcto",
                "Tensión eliminada"
            )

            self.list_all_tensions()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def average_tension(self):

        try:

            patient_reference = (
                self.get_selected_patient_id()
            )

            result = self.controller.get_average(
                patient_reference
            )

            if result is None:

                messagebox.showinfo(
                    "Sin datos",
                    "No hay tensiones"
                )

            else:

                self.results.delete("1.0", tk.END)

                self.results.insert(
                    tk.END,
                    f"Media sistólica: "
                    f"{result[0]}\n"
                    f"Media diastólica: "
                    f"{result[1]}"
                )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def last_tension(self):

        try:

            patient_reference = (
                self.get_selected_patient_id()
            )

            result = self.controller.get_last_tension(
                patient_reference
            )

            if result is None:

                messagebox.showinfo(
                    "Sin datos",
                    "No hay tensiones"
                )

            else:

                self.results.delete("1.0", tk.END)

                self.results.insert(
                    tk.END,
                    f"Última toma:\n"
                    f"Sistólica: "
                    f"{result['systolic']}\n"
                    f"Diastólica: "
                    f"{result['diastolic']}\n"
                    f"Fecha: "
                    f"{result['date']}\n"
                    f"Estado: "
                    f"{result['state']}\n"
                    f"Descripción: "
                    f"{result['description']}\n"
                    f"En rango: "
                    f"{result['in_range']}"
                )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def run(self):

        self.refresh_patient_menu()

        self.refresh_tension_menu()

        self.root.mainloop()