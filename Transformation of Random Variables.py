import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x, y, u, v = sp.symbols('x y u v')

equation1_str = input("Enter the first equation : ")
equation2_str = input("Enter the second equation : ")
joint_pdf_xy_str = input("Enter the joint pdf of x,y :")
limit_x = input("Enter the limits for x: ")
limit_y = input("Enter the limits for y: ")


eq1 = sp.sympify(equation1_str)
eq2 = sp.sympify(equation2_str)
joint_pdf_xy=sp.sympify(joint_pdf_xy_str)
 

eq1 = eq1.subs('e', sp.E)
eq2 = eq2.subs('e', sp.E)
joint_pdf_xy = joint_pdf_xy.subs('e', sp.E)

equation1 = sp.Eq(u, eq1)
equation2 = sp.Eq(v, eq2)



solution = sp.solve((equation1, equation2), (x, y))
if isinstance(solution,list):
    solution=list(solution[0])
else:
    solution=list(solution.values())


print("Solution:")
print(solution)


equation1 = sp.Eq(x, solution[0])
equation2 = sp.Eq(y, solution[1])


variables = [u, v]


jacobian_matrix = sp.Matrix([[sp.diff(eq.rhs, var) for var in variables] for eq in [equation1, equation2]])


print("Corrected Jacobian Matrix:")
print(jacobian_matrix)



jacobian_det = sp.det(jacobian_matrix)



joint_pdf_uv = joint_pdf_xy.subs({x: solution[0], y: solution[1]}) * jacobian_det



print("Joint PDF of U and V:")
print(joint_pdf_uv)

lower_limit_x = 0
upper_limit_x = 0
lower_limit_y = 0
upper_limit_y = 0

def convert_limits(expression_x, limit_x,expression_y,limit_y):
    
    u, v, x, y = sp.symbols('u v x y')

    
    constraint1 = sp.Eq(x, expression_x)
    constraint2 = sp.Eq(y, expression_y)

    
    u = sp.solve(constraint1, u)[0]
    v = sp.solve(constraint2, v)[0]

    
    lower_limit_x, upper_limit_x = limit_x.split(',')
    lower_limit_y, upper_limit_y = limit_y.split(',')

    
    lower_limit_u = u.subs(x, lower_limit_x)
    upper_limit_u = u.subs(x, upper_limit_x)
    lower_limit_v = v.subs(y, lower_limit_y)
    upper_limit_v = v.subs(y, upper_limit_y)

    return lower_limit_u, upper_limit_u,lower_limit_v,upper_limit_v


expression_x = solution[0] 
expression_y = solution[1] 


lower_limit_u, upper_limit_u,lower_limit_v,upper_limit_v = convert_limits(expression_x, limit_x,expression_y,limit_y)


print("Limit on u:", lower_limit_u,upper_limit_u)
print("Limit on v:", lower_limit_v,upper_limit_v)


marginal_pdf_u = sp.integrate(joint_pdf_uv, (v, lower_limit_v, upper_limit_v))


print("Marginal PDF of U:")
print(marginal_pdf_u)


marginal_pdf_v = sp.integrate(joint_pdf_uv, (u, lower_limit_u,upper_limit_u))


print("Marginal PDF of V:")
print(marginal_pdf_v)



joint_pdf_xy = lambda x, y: x + y
joint_pdf_uv = lambda u, v:(u/v + v)/v


x_values = np.linspace(0, 1, 50)
y_values = np.linspace(0, 1, 50)
u_values = np.linspace(0, 1, 50)
v_values = np.linspace(0, 1, 50)


X, Y = np.meshgrid(x_values, y_values)
U, V = np.meshgrid(u_values, v_values)



Z_xy = joint_pdf_xy(X, Y)
Z_uv = joint_pdf_uv(U, V)


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.contourf(X, Y, Z_xy, cmap='viridis')
plt.title('Joint PDF of X, Y')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()


plt.subplot(1, 2, 2)
plt.contourf(U, V, Z_uv, cmap='plasma')
plt.title('Joint PDF of U, V')
plt.xlabel('u')
plt.ylabel('v')
plt.colorbar()


plt.tight_layout()


plt.suptitle("Transformation of Random Variable")
plt.show()





