from mod_reports import generate_text_report

data = input("Enter data separated by commas: ")
try:
    data = list(map(int, data.split(',')))
    report = generate_text_report(data)
    for item in report:
        print(item)
except ValueError:
    print("Wrong data")
