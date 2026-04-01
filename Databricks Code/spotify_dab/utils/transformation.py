class reusable:

    def dropColoumns(self,df,coloumns):
        df = df.drop(*coloumns)
        return df