class Row:
    """Facilitates row representation after DB query"""
    def __init__(self, cols, row):
        for i, col in enumerate(cols):
            setattr(self, col, row[i])
