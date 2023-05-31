from dataclasses import dataclass
import pandas as pd
from bs4 import BeautifulSoup
import requests


@dataclass
class CongressHandles:
    url: str
    _type: str

    def get_content(self):
        return requests.get(self.url)

    def get_tables(self, page_source):
        soup = BeautifulSoup(page_source, "html.parser")
        return soup.find_all("table")

    def read_table(self, table):
        df = pd.DataFrame(columns=[self._type, "Link", "State", "Party"])
        for row in table.find_all("tr"):
            row_data = []
            for j,cell in enumerate(row.find_all("td")):
                if j == 0:
                    link = cell.find("a")
                    if link:
                        row_data.append(cell.get_text())
                        row_data.append(link["href"])
                    else:
                        row_data.append(cell.get_text())
                        row_data.append(None)
                else:
                    if cell.get_text() == self._type:
                        row_data.append(None)
                    row_data.append(cell.get_text())
            df.loc[len(df)] = row_data
        return df

    def get_handles(self):
        tables = self.get_tables(self.get_content().content)
        df = pd.concat([self.read_table(table) for table in tables])
        return df.loc[df[self._type].notnull()].reset_index(drop=True)
