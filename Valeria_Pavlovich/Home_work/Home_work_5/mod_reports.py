def generate_text_report(data):
    avg = sum(data) / len(data)
    data_count = len(data)
    return ['Report: ',
            '=======',
            f'Total records: {data_count}',
            f'Average: {avg:.2f}',
            f'Maximum: {max(data)}']
