### Simple Personal Financial Data App
#### Python App for Treating, analyzing and visualizing Personal Financial Data on Flask and Plotly Web App

This simple Python App applies Pandas, plotly, flask and dash functionalities to create a simple yet insightfull 
web app for analysing expenses data:

- monthly
- by category of purchase
- by type of payment


Feel free to locally use it for your own personal data expenses analysis. :)

#### Data Input
##### The App expects a simple CSV tabular schema of purchase events:
| Column | Description | Column-type |
|--------| ------------| ----------|
| date | date of purchase on format YYYY-MM-DD | string |
| payment_type | type of payment (debit, credit..) | string |
| price | value of the purchase/expanse | string |
| category | what type of purchase/expanse? (ex: food, gasoline, rent) | string |
| subcategory | is there a sub-type worth monitoring? (ex: groceries, restaurant, transport) | string |

##### Running the Project

- Set a file .env inside *app* folder with a configured env var FINANCIAL_DATA_PATH=your-csv-file-path.
- Make sure all dependencies are installed:
```bash
 pip install -r ./app/requirements.txt
 ```
- Make sure that your data column names matches the ones 
on the tools.treatment.treat_data if not, adapt either script or data schema.
- To run the app:
```python
python3 ./app/main.py
```
- Your dashboard will be available at http://127.0.0.1:8050/.
