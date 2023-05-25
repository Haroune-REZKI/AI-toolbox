import tkinter as tk
from tkinter import messagebox

# class Constraint():
#     def __init__(self, variables):
#         self.variables = variables
#     def satisfied(self, assignment):
#         #implementation will be overwritten later on
#         pass

class CSP():
    def __init__(self, variables, domains, constraints):
        self.variables = variables  # list of variables
        self.domains = domains  # dictionary of domains
        self.constraints = {variable: [] for variable in variables}  # initialize constraints dictionary

        for constraint in constraints:
            self.add_constraint(constraint)

    def consistent(self, variable, assignment):
        for constraint in self.constraints[variable]:
            if not constraint["satisfied"](assignment):
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment
        unassigned = [v for v in self.variables if v not in assignment]
        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # if we are still consistent, we recurse
            if self.consistent(first, local_assignment):
                result = self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None

    def add_constraint(self, constraint):
        for variable in constraint["variables"]:
            if variable not in self.variables:
                raise LookupError("variables in constraint not in csp")
            else:
                self.constraints[variable].append(constraint)

def map_coloring_satisfied(assignment, place1, place2):
    if place1 not in assignment or place2 not in assignment:
        return True
    return assignment[place1] != assignment[place2]

# Your existing code for Constraint, CSP, and MapColoringConstraint classes


def add_region():
    region = region_entry.get()
    if region not in csp.variables:
        csp.variables.append(region)
        csp.constraints[region] = []
        region_listbox.insert(tk.END, region)
    else:
        messagebox.showerror("Error", "Region already exists!")

def add_domain():
    domain = domain_entry.get()
    if domain not in csp.domains.values():
        for region in csp.variables:
            if region not in csp.domains:
                csp.domains[region] = []
            csp.domains[region].append(domain)
        domain_listbox.insert(tk.END, domain)
    else:
        messagebox.showerror("Error", "Domain already exists!")

def add_constraint():
    region1 = constraint_region1_entry.get()
    region2 = constraint_region2_entry.get()
    if region1 in csp.variables and region2 in csp.variables:
        constraint = {
            "variables": [region1, region2],
            "satisfied": lambda assignment: map_coloring_satisfied(assignment, region1, region2)
        }
        csp.add_constraint(constraint)
        constraint_listbox.insert(tk.END, f"{region1} - {region2}")
    else:
        messagebox.showerror("Error", "Invalid regions for constraint!")

def solve_csp():
    result = csp.backtracking_search()
    if result is not None:
        output = "\n".join([f"{region}: {color}" for region, color in result.items()])
        messagebox.showinfo("Solution", output)
    else:
        messagebox.showerror("Error", "No solution found!")

# Initialize CSP
csp = CSP([], {}, [])

# Create GUI
root = tk.Tk()
root.title("Map Coloring Solver")

# Set colors and formatting
root.configure(bg="#F5F5F5")  # Set background color of the root window

# Create a frame for the inputs
input_frame = tk.Frame(root, bg="#F5F5F5")
input_frame.pack(pady=20)

# Region input
region_label = tk.Label(input_frame, text="Region:", bg="#F5F5F5")
region_label.grid(row=0, column=0, padx=10, pady=10)
region_entry = tk.Entry(input_frame)
region_entry.grid(row=0, column=1, padx=10, pady=10)
region_button = tk.Button(input_frame, text="Add Region", command=add_region, bg="#3F51B5", fg="white")
region_button.grid(row=0, column=2, padx=10, pady=10)

# Domain input
domain_label = tk.Label(input_frame, text="Domain:", bg="#F5F5F5")
domain_label.grid(row=1, column=0, padx=10, pady=10)
domain_entry = tk.Entry(input_frame)
domain_entry.grid(row=1, column=1, padx=10, pady=10)
domain_button = tk.Button(input_frame, text="Add Domain", command=add_domain, bg="#3F51B5", fg="white")
domain_button.grid(row=1, column=2, padx=10, pady=10)

# Constraint input
constraint_region1_label = tk.Label(input_frame, text="Constraint Region 1:", bg="#F5F5F5")
constraint_region1_label.grid(row=2, column=0, padx=10, pady=10)
constraint_region1_entry = tk.Entry(input_frame)
constraint_region1_entry.grid(row=2, column=1, padx=10, pady=10)

constraint_region2_label = tk.Label(input_frame, text="Constraint Region 2:", bg="#F5F5F5")
constraint_region2_label.grid(row=3, column=0, padx=10, pady=10)
constraint_region2_entry = tk.Entry(input_frame)
constraint_region2_entry.grid(row=3, column=1, padx=10, pady=10)

constraint_button = tk.Button(input_frame, text="Add Constraint", command=add_constraint, bg="#3F51B5", fg="white")
constraint_button.grid(row=3, column=2, padx=10, pady=10)

# Create a frame for the lists and solve button
result_frame = tk.Frame(root, bg="#F5F5F5")
result_frame.pack(pady=20)

# Listboxes
region_listbox = tk.Listbox(result_frame)
region_listbox.grid(row=0, column=0, padx=10, pady=10)
domain_listbox = tk.Listbox(result_frame)
domain_listbox.grid(row=0, column=1, padx=10, pady=10)
constraint_listbox = tk.Listbox(result_frame)
constraint_listbox.grid(row=0, column=2, padx=10, pady=10)

# Solve button
solve_button = tk.Button(root, text="Solve", command=solve_csp, bg="#3F51B5", fg="white")
solve_button.pack(pady=20)

# Set colors and formatting for labels
labels = [region_label, domain_label, constraint_region1_label, constraint_region2_label]
for label in labels:
    label.configure(font=("Arial", 12), fg="black")

# Set colors and formatting for entry fields
entry_fields = [region_entry, domain_entry, constraint_region1_entry, constraint_region2_entry]
for entry in entry_fields:
    entry.configure(font=("Arial", 12), fg="black")

# Set colors and formatting for listboxes
listboxes = [region_listbox, domain_listbox, constraint_listbox]
for listbox in listboxes:
    listbox.configure(font=("Arial", 12), fg="black", bg="white")

# Set colors and formatting for buttons
buttons = [region_button, domain_button, constraint_button, solve_button]
for button in buttons:
    button.configure(font=("Arial", 12))

root.mainloop()
