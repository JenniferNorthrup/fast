from fastapi import APIRouter

employees_router = APIRouter()

@employees_router.get("/employees/{emp_id}")
async def get_emp_by_id(emp_id: int):
    return [{
        "empId": emp_id,
        "firstName": "Bob",
        "lastName": "Smith"
    }]
