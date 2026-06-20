from django.shortcuts import redirect, render
from django.views import View
from .models import Employee, Department

# Create your views here.
# def home(request):
#     return render(request, 'home.html')

class HomeView(View):
    def get(self, request):
        try :
            emps = Employee.objects.all() # 10 sec
            return render(request, 'home.html', {'empList' : emps})
        except e as Exception:
            pass


# def create(request):
#     if request.method == 'POST':
#         pass
    
#     return render(request, 'create.html')

class CreateView(View):

    def get(self, request):
        depts = Department.objects.all()
        return render(request, 'create.html', {'deptList': depts})

    def post(self, request):

        if request.POST["Register"] == "Register":

            Ename = request.POST["Ename"]
            Password = request.POST["Password"]
            Gender = request.POST["Gender"]
            Phone = request.POST["Phone"]
            Email = request.POST["Email"]
            DOB = request.POST["DOB"]
            Salary = int(request.POST["Salary"])
            Address = request.POST["Address"]
            DeptNo = int(request.POST["DeptNo"])

            

            Employee.objects.create(
                Ename=Ename,
                Password=Password,
                Gender=Gender,
                Phone=Phone,
                Email=Email,
                DOB=DOB,
                Salary=Salary,
                Address=Address,
                DeptNo_id=DeptNo
            )

        return redirect('home')

# def edit(request, empid):
#     return render(request, 'edit.html')

class EditView(View):
    def get(self, request, empid):
        depts = Department.objects.all()
        employee = Employee.objects.get(EmpId = int(empid))
        return render(request, 'edit.html', {'deptList': depts, 'emp' : employee})

    def post(self, request, empid):
        if request.POST["Update"] == "Update":
            EmpId = request.POST["EmpId"]
            Ename = request.POST["Ename"]
            Password = request.POST["Password"]
            Gender = request.POST["Gender"]
            Phone = request.POST["Phone"]
            Email = request.POST["Email"]
            DOB = request.POST["DOB"]
            Salary = int(request.POST["Salary"])
            Address = request.POST["Address"]
            DeptNo = int(request.POST["DeptNo"])

            emp = Employee(
                EmpId=EmpId,
                Ename=Ename,
                Password=Password,
                Gender=Gender,
                Phone=Phone,
                Email=Email,
                DOB=DOB,
                Salary=Salary,
                Address=Address,
                DeptNo_id=DeptNo)
            
            emp.save()

        return redirect('home')
        

# def delete(request, empid):
#     return render(request, 'delete.html')

class DeleteView(View):
    def get(self, request, empid):
        depts = Department.objects.all()
        employee = Employee.objects.get(EmpId = int(empid))
        return render(request, 'delete.html', {'deptList': depts, 'emp' : employee})

    def post(self, request, empid):
        if request.POST["Delete"] == "Do you really want to delete?":
           emp = Employee.objects.get(EmpId = int(empid))
           emp.delete()

        return redirect('home')