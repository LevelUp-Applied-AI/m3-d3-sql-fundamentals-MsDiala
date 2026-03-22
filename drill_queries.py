import sqlite3

def top_departments(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        query = """
        SELECT d.name, SUM(e.salary) as total_salary
        FROM employees e
        JOIN departments d ON e.dept_id = d.dept_id
        GROUP BY d.dept_id
        ORDER BY total_salary DESC
        LIMIT 3
        """
        cursor.execute(query)
        results = cursor.fetchall()
        return results

def employees_with_projects(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        query = """
        SELECT e.name, p.name
        FROM employees e
        JOIN project_assignments pa ON e.employee_id = pa.employee_id
        JOIN projects p ON pa.project_id = p.id
        """
        cursor.execute(query)
        results = cursor.fetchall()
        return results

def salary_rank_by_department(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        query = """
        SELECT e.name, d.name, e.salary, RANK() OVER(PARTITION BY e.dept_id ORDER BY e.salary DESC) as rank
        FROM employees e
        JOIN departments d ON e.dept_id = d.dept_id
        ORDER BY d.name, rank
        """
        cursor.execute(query)
        results = cursor.fetchall()
        return results

