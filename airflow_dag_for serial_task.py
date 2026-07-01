from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils import timezone
from datetime import datetime, timedelta
def hello_world_py(*args, **kwargs):
    print('Hello World from PythonOperator')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # 'email_on_failure': False,
    # 'email_on_retry': False,
    # 'email': ['your-email@example.com'],
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'first_dag_for_seq_tasks',
    default_args=default_args,
    description='A dummy DAG',
    start_date=datetime(2026, 6, 28),
    schedule="*/1 * * * *",   # use 'schedule' instead of 'schedule_interval'
    catchup=False,
    tags=['dev'],
)


t1 = BashOperator(
    task_id='Print_From_Bash_Operator',
    bash_command='echo "Hello World from BashOperator"',
    dag=dag,
)

t2 = PythonOperator(
    task_id='Print_From_Python_Operator',
    python_callable=hello_world_py,
    dag=dag,
)

t1 >> t2  # Specifies that t2 should follow t1