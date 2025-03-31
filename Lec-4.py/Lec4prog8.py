student = {
        "name": "Advait Kulkarni",
        "subject" : {
            "phy" : 97,
            "chem" : 98,
            "math" : 95,
        }
}

new_dict = {"city" : "delhi"}
student.update(new_dict)

print(student)