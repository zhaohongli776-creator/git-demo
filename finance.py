class Finance:
    def __init__(self, id, amount, type, note, category, date):
        self.id = id
        self.amount = amount
        self.type = type
        self.note = note
        self.category = category
        self.date = date
    def recode_income():
        recodes = {
            "id": id,
            "amount": amount,
            "type": type,
            "note": note,
            "category": category,
            "date": date,
    }
        return recodes
    def recode_outcome():

        recodes = {
        "id": id,
        "amount": amount,
        "type": type,
        "note": note,
        "date": date,
    }
        return recodes
    def summerize_records():
        total_income = 0
        total_outcome = 0
        for record in records:
            if record.type == "收入":
                total_income += record.amount
            elif record.type == "支出":
                total_outcome += record.amount
        return total_income, total_outcome
    def summarize_by_category():
        category_summary = {}
        for record in records:
            if record.category not in category_summary:
                category_summary[record.category] = 0
            category_summary[record.category] += record.amount
        return category_summary
    def delete_record(record_id):
        for record in records:
            if record.id == record_id:
                records.remove(record)
                return True
        return False
    def view_all_records():
        return records
    def view_record(record_id):
        for record in records:
            if record.id == record_id:
                return record
        return None
    def update_record(record_id, amount=None, type=None, note=None, category=None, date=None):
        for record in records:
            if record.id == record_id:
                if amount is not None:
                    record.amount = amount
                if type is not None:
                    record.type = type
                if note is not None:
                    record.note = note
                if category is not None:
                    record.category = category
                if date is not None:
                    record.date = date
                return True
        return False
    def search_records(keyword):
        result = []
        for record in records:
            if (keyword in str(record.amount) or
                keyword in record.type or
                keyword in record.note or
                keyword in record.category or
                keyword in record.date):
                result.append(record)
        return result
    def sort_records(by="date", ascending=True):
        if by == "date":
            records.sort(key=lambda x: x.date, reverse=not ascending)
        elif by == "amount":
            records.sort(key=lambda x: x.amount, reverse=not ascending)
        elif by == "type":
            records.sort(key=lambda x: x.type, reverse=not ascending)
        elif by == "category":
            records.sort(key=lambda x: x.category, reverse=not ascending)
        return records