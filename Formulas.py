from os import system
from time import sleep 
import platform
import numpy as np
import math

def LAW():
        system('clear') if platform.system()=='Linux' else system('cls')
        print('Formulas :- ')
        print('')
        print('1 : v=u+at')
        print('2 : v^2=u^2+2as')
        print('3 : s=ut+1/2(a(t^2))')
        print('4 : Go back to main')
        print('')
        
        x2=int(input('Select category: '))

        if x2==1:
                LAW_1()
        elif x2==2:
                LAW_2()
        elif x2==3:
                LAW_3()
        elif x2==4:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid choice !')
                print('')
                sleep(2)
                system('clear') if platform.system()=='Linux' else system('cls')


#calculation of v=u+at
def LAW_1():
        system('clear') if platform.system()=='Linux' else system('cls')
        print('Select operation :- ')
        print('')
        print('1 : calculate v')
        print('2 : calculate a')
        print('3 : calculate t')
        print('4 : calculate u')
        print('5 : Go back to main')
        print('')

        LAW_1_input=int(input('Select category: '))

        if LAW_1_input==1:
                system('clear') if platform.system()=='Linux' else system('cls')
                u=float(input('Enter the value of u: '))
                a=float(input('Enter the value of a: '))
                t=float(input('Enter the value of t: '))
                
                v=u+a*t
                print('Value of Final Velocity (v) = ',v)
                input('Press Enter to continue ')

        elif LAW_1_input==2:
                system('clear') if platform.system()=='Linux' else system('cls')
                u=float(input('Enter the value of u: '))
                v=float(input('Enter the value of v: '))
                t=float(input('Enter the value of t: '))
                
                a=(v-u)/t
                print('Value of acceleration (a) = ',a)
                input('Press Enter to continue ')
                
        elif LAW_1_input==3:
                system('clear') if platform.system()=='Linux' else system('cls')
                u=float(input('Enter the value of u: '))
                v=float(input('Enter the value of v: '))
                a=float(input('Enter the value of a: '))

                t=(v-u)/a
                print('Value of Time (T) = ',t)
                input('Press Enter to continue ')
                
        elif LAW_1_input==4:
                system('clear') if platform.system()=='Linux' else system('cls')
                v=float(input('Enter the value of v: '))
                a=float(input('Enter the value of a: '))
                t=float(input('Enter the value of t: '))

                u=v-a*t
                print('Value of Initial Velocity (u) = ',u)
                input('Press Enter to continue ')
                
        elif LAW_1_input==5:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid choice !')
                print('')
                sleep(2)
                system('clear') if platform.system()=='Linux' else system('cls')

#calculation of v^2=u^2+2as
def LAW_2():
        system('clear') if platform.system()=='Linux' else system('cls')
        print('Select operation :- ')
        print('')
        print('1 : calculate v')
        print('2 : calculate a')
        print('3 : calculate s')
        print('4 : calculate u')
        print('5 : Go back to main')
        print('')

        LAW_2_input=int(input('Select category: '))

        if LAW_2_input==1:
                system('clear') if platform.system()=='Linux' else system('cls')
                u=float(input('Enter the value of u: '))
                a=float(input('Enter the value of a: '))
                s=float(input('Enter the value of s: '))

                v=np.sqrt((u*u)+2*a*s)
                print('Value of velocity(v)',v)
                input('Press Enter to continue ')

        elif LAW_2_input==2:
                system('clear') if platform.system()=='Linux' else system('cls')
                v=float(input('Enter the value of v: '))
                u=float(input('Enter the value of u: '))
                s=float(input('Enter the value of s: '))

                a=((v*v)-(u*u))/2*s
                print('Value of acceleration (a): ',a)
                input('Press Enter to continue ')

        elif LAW_2_input==3:
                system('clear') if platform.system()=='Linux' else system('cls')
                v=float(input('Enter the value of v: '))
                u=float(input('Enter the value of u: '))
                a=float(input('Enter the value of a: '))

                s=((v*v)-(u*u))/2*a
                print('Value of distance (s): ',s)
                input('Press Enter to continue ')

        elif LAW_2_input==4:
                system('clear') if platform.system()=='Linux' else system('cls')
                v=float(input('Enter the value of v: '))
                a=float(input('Enter the value of a: '))
                s=float(input('Enter the value of s: '))

                u=np.sqrt((v*v)-2*a*s)
                print('Value of distance (s): ',s)
                input('Press Enter to continue ')

        elif LAW_2_input==5:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid choice !')
                print('')
                sleep(2)
                system('clear') if platform.system()=='Linux' else system('cls')

#calculation of s=ut+1/2(a(t^2))
def LAW_3():
        system('clear') if platform.system()=='Linux' else system('cls')
        print('Select operation :- ')
        print('')
        print('1 : calculate u')
        print('2 : calculate a')
        print('3 : calculate t')
        print('4 : Go back to main')
        print('')

        LAW_3_input=int(input('Select category: '))

        if LAW_3_input==1:
                system('clear') if platform.system()=='Linux' else system('cls')
                t=float(input('Enter the value of t: '))
                a=float(input('Enter the value of a: '))
                s=float(input('Enter the value of s: '))

                u=(((2*s)-(a*t))/2)
                print('Value of initial velocity(u)',u)
                input('Press Enter to continue ')
        
        elif LAW_3_input==2:
                system('clear') if platform.system()=='Linux' else system('cls')
                t=float(input('Enter the value of t: '))
                u=float(input('Enter the value of u: '))
                s=float(input('Enter the value of s: '))

                a=(2*(s-(u*t))/t*t)
                print('Value of acceleration(a)',a)
                input('Press Enter to continue ')
        
        elif LAW_3_input==3:
                system('clear') if platform.system()=='Linux' else system('cls')
        
                u=float(input('Enter the value of u: '))
                a=float(input('Enter the value of a: '))
                s=float(input('Enter the value of s: '))

                t=(2*s)/(u+(np.sqrt((u*u)+2*a*s)))
                print('Value of time(t)',t)
                input('Press Enter to continue ')

        elif LAW_3_input==4:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid choice !')
                print('')
                sleep(2)
                system('clear') if platform.system()=='Linux' else system('cls')
        
# Centroid:
def CG():
        system('clear') if platform.system()=='Linux' else system('cls')
        print('Formulas :- ')
        print('')
        print('1 : Centroid of Plane Figure and Area ')
        print('2 : Surface Area ')
        print('3 : Go back to main')
        print('')
        
        x1=int(input('Select category: '))

        if x1==1:
                CG_1()
        elif x1==2:
                CG_2()
        elif x1==3:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        
        else:
                print('Invalid Choice !')
                print('')
                sleep(1)
                system('clear')



#calculation of centroid
def CG_1():
        system('clear') if platform.system()=='Linux' else system('cls')
        print('Select Operation :-')
        print('')
        print('1 : Centroid of Rectangle')
        print('2 : Centroid of Traingle')
        print('3 : Centroid of Semi-circular area')
        print('4 : Centroid of Circular sector')
        print('5 : Go back to main')
        print('')

        CG_1_input=int(input('Select category: '))

        if CG_1_input==1:
                
                system('clear') if platform.system()=='Linux' else system('cls')
                print('Select plane surface: ')
                print('')
                print('1 : Horizantally')
                print('2 : Vertically')
                print('3 : Go back to main')
                print('')

                CG_1a_input=int(input('Select your surface: '))
                
                if CG_1a_input==1:
                    system('clear') if platform.system()=='Linux' else system('cls')
                    print('')
                    l=int(input('Enter the length of Reactangle: '))
                    b=int(input('Enter the breadth of Rectangle: '))

                    x=l/2
                    y=b/2
                    print('For X axis and Y axis:',(x,y))
                    input('Press Enter to continue ')
             
                elif CG_1a_input==2:
                    system('clear') if platform.system()=='Linux' else system('cls')
                    print('')
                    l=int(input('Enter the length of Reactangle: '))
                    b=int(input('Enter the breadth of Rectangle: '))

                    x=b/2
                    y=l/2
                    print('For X axis and Y axis:',(x,y))
                    print('')
                    input('Press Enter to continue ')

                elif CG_1a_input==3:
                    system('clear') if platform.system()=='Linux' else system('cls')    
                    main()
                    
                else:
                    print('Invalid opt !')
                    print('')
                    sleep(2)
                    system('clear') if platform.system()=='Linux' else system('cls')

                        

        elif CG_1_input==2:
                system('clear') if platform.system()=='Linux' else system('cls')
                h=int(input('Enter the value of h: '))
                b=int(input('Enter the value of b: '))
                print('')
                y=h/3
                area=b*h/2
                print('Centroid of traingle along the x axis ','y :',y,'area :',area)
                input('Press Enter to continue ')

        elif CG_1_input==3:
               system('clear') if platform.system()=='Linux' else system('cls')
               r=int(input('Enter the radius of circle: '))
               print('')
               print(':: With X-bar = 0 ::')
               print('')

               y=(4*r)/3*3.14
               Area=(3.14*r*r)/2
               print('Centroid of the Semi-circle ','Y-bar= ',y,'and Area= ',Area)
               print('')
               input('Press Enter to continue ')
               
        elif CG_1_input==4:
               system('clear') if platform.system()=='Linux' else system('cls')
               r=int(input('Enter the radius: '))
               print('')
               print('1 :30º')
               print('2 :60º')
               print('3 :90º')
               print('4 :Go back to main')
               print('')

               CS_1a_input=int(input('Select the degree: '))

               if CS_1a_input==1:
                               system('clear') if platform.system()=='Linux' else system('cls')
                               print('')
                               x=(2*r*0.5)/3*0.5
                               Area=0.5*r*r 
                               print('Value of X-bar along x axis: ',x,'Area: ',Area)
                               print('')
                               input('Press Enter to continue ')

               elif CS_1a_input==2:
                               system('clear') if platform.system()=='Linux' else system('cls')
                               print('')
                               x=(2*r*0.86602540378)/3*0.86602540378
                               Area=0.86602540378*r*r
                               print('Value of X-bar along X axis: ',x,'Area: ',Area)
                               print('')
                               input('Press Enter to continue ')
                       
               elif CS_1a_input==3:
                               system('clear') if platform.system()=='Linux' else system('cls')
                               print('')
                               x=(2*r*1)/3*1
                               Area=1*r*r
                               print('Value of X-bar along X axis: ',x,'Area',Area)
                               print('')
                               input('Press Enter to continue ')
                               
               elif CS_1a_input==4:
                               system('clear') if platform.system()=='Linux' else system('cls')
                               main()
                               
               else:
                               print('Invalid choice !')
                               print('')
                               sleep(2)
                               system('clear') if platform.system()=='Linux' else system('cls')
                               

#Surface Area
def CG_2():
         system('clear') if platform.system()=='Linux' else system('cls')
         print('Select Operation: ') 
         print('')
         print('1 :Surface Area of Cube ')
         print('2 :Surface Area of Cuboid ')
         print('3 :Surface Area of Cylinder ')
         print('4 :Surface Area of Sphere ')
         print('5 :Surface Area of Cone ')
         print('6 :Go back to main')
         print('')

         CS_2_input=int(input('Your Choice: '))

         if CS_2_input==1:
                 system('clear') if platform.system()=='Linux' else system('cls')
                 print('')
                 print('1 :Surface Area of Cube ')
                 print('')
                 a=float(input('Enter the value of a: '))
                 print('')

                 cube=6*a*a
                 print('The Surface area of Cube: ',cube)
                 input('Press Enter to continue ')
                 
         elif CS_2_input==2:
                 system('clear') if platform.system()=='Linux' else system('cls')
                 print('')
                 print('2 :Surface Area of Cuboid ')
                 print('')
                 l=float(input('Enter the length: '))
                 b=float(input('Enter the width: '))
                 h=float(input('Enter the height: '))
                 print('')

                 cuboid=2*l*b+2*l*h+2*b*h
                 print('The Surfae area of Cuboid: ',cuboid)
                 input('Press Enter to continue ')
                 
         elif CS_2_input==3:
                 
                system('clear') if platform.system()=='Linux' else system('cls')
                print('')
                print('3 :Surface Area of Cylinder ')
                print('')
                r=float(input('Enter the radius: '))
                h=float(input('Enter the height: '))
                pi=3.14
                cylinder=2*pi*r*h+2*pi*r*r
                
                print('')
                print('The Total surface area of cylinder: ',cylinder)
                input('Press Enter to continue ')
                
         elif CS_2_input==4:
                system('clear') if platform.system()=='Linux' else system('cls')
                print('')
                print('4 :Surface Area of Sphere ')
                print('')
                r=float(input('Enter the radius: '))
                pi=3.14
                sphere=4*pi*r*r
                
                print('')  
                print('Surface area of sphere: ',sphere)
                input('Press Enter to continue ')
                
         elif CS_2_input==5:
                
                system('clear') if platform.system()=='Linux' else system('cls')
                print('')
                print('5 :Surface Area of Cone ')
                print('')
                r=float(input('Enter the radius: '))
                s=float(input('Enter the slant height: '))
                pi=3.14
                cone=pi*r*s+pi*r*r

                print('')
                print('Surface area of cone: ',cone)
                input('Press Enter to continue ')
                          
         elif CS_2_input==6:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
                
         else:
                print('Invalid choice !')
                print('')
                sleep(2)
                system('clear') if platform.system()=='Linux' else system('cls')
                
def MIRROR():
        system('clear') if platform.system=='Linux' else system('cls')
        print('Formulas:')
        print('')
        print('1: Concave')
        print('2: Convex')
        print('3: Go back to main menu')
        print('')
        
        x=int(input('Select Category:'))
        if x==1:
                CONCAVE()
        elif x==2:
                CONVEX()
        elif x==3:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print("Invalid choice!")
                sleep(2)
                system('clear') if platform.system=='Linux' else system('cls')
        
def CONCAVE(): 
        system('clear') if platform.system=='Linux' else system('cls')
        print('Select operation:')
        print('')
        print('1: Calculate u')
        print('2: Calculate v')
        print('3: Calculate f')
        print('4: Go back to main menu')
        print('')
        
        CONCAVE_input=int(input('Select category:'))
        if CONCAVE_input==1:
                system('clear') if platform.system=='Linux' else system('cls')
                print('')
                u=float(input('Enter the value of u:'))
                v=float(input('Enter the value of v:'))
                f=float(input('Enter the value of f:'))
                f=(u*v)/(u+v)
                print('Value of focal length for concave mirror is:',f)
                input('Press Enter to continue ')
                
        elif CONCAVE_input==2:
                system('clear') if platform.system=='Linux' else system('cls')
                print('')
                u=float(input('Enter the value of u:'))
                v=float(input('Enter the value of v:'))
                f=float(input('Enter the value of f:'))
                u=(v*f)/(v-f)
                print('Value of focal length for convex mirror is:',u)
                input('Press Enter to continue ')
                
        elif CONCAVE_input==3:
                system('clear') if platform.system=='Linux' else system('cls')
                print('')
                u=float(input('Enter the value of u:'))
                v=float(input('Enter the value of v:'))
                f=float(input('Enter the value of f:'))
                v=(u*f)/(u-f)
                print('Value :',v)
                print('')
                input('Press Enter to continue ')
        elif CONCAVE_input==4:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print("Invalid choice")
                print('')
                sleep(2)
                system('clear') if platform.system=='Linux' else system('cls')

def CONVEX():
        system('clear') if platform.system=='Linux' else system('cls')
        print('Select operation:')
        print('')                                      
        print('1: Calculate u')
        print('2: Calculate v')
        print('3: Calculate f')
        print('4: Go back to main menu')
        print('')
        CONVEX_input=int(input('Select Category:'))
        if CONVEX_input==1:
                system('clear') if platform.system=='Linux' else system('cls')
                print('')
                u=float(input('Enter the value of u:'))
                v=float(input('Enter the value of v:'))
                f=float(input('Enter the value of f:'))
                print('')
                f=(u*v)/(u-v)
                print('Value of focal length for convex mirror is:',f)
                input('Press Enter to continue ')
                
        elif CONVEX_input==2:
                system('clear') if platform.system=='Linux' else system('cls')
                u=float(input('Enter the value of u:'))
                v=float(input('Enter the value of v:'))
                f=float(input('Enter the value of f:'))
                u=((-v)*(-f))/((-v)-(-f))
                print('Value of object distance is:',u)
                input('Press Enter to continue ')
                
        elif CONVEX_input==3:
                system('clear') if platform.system=='Linux' else system('cls')
                u=float(input('Enter the value of u:'))
                v=float(input('Enter the value of v:'))
                f=float(input('Enter the value of f:'))
                print('')
                v=(u*(-f))/(u-(-f))
                print('Value: ',v)
                print('')
                input('Press Enter to continue ')
                
        elif CONVEX_input==4:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print("Invalid choice")
                sleep(2)
                print('')
                system('clear') if platform.system=='Linux' else system('cls')
                
#VOLUME OF OBJECTS AND AREAS
def VOL():
        system('clear') if platform.system()=='Linux'else system('cls')
        print('Formulas :- ')
        print('')
        print('1 : Volume of cube')
        print('2 : Volume of Cuboid')
        print('3 : Volume of sphere')
        print('4 : Area of square')
        print('5 : Area of triangle')
        print('6 : Area of rectangle')
        print('7 : GO back  to main menu')
        print('')
        
        x2=int(input('Select category: '))
        print('')

        if x2==1:
                VOL_1()
        elif x2==2:
                VOL_2()
        elif x2==3:
                VOL_3()
        elif x2==4:
                VOL_4()
        elif x2==5:
                VOL_5()
        elif x2==6:
                VOL_6()
        elif x2==7:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid choice !')
                print('')
                sleep(2)
                system('clear') if platform.system()=='Linux'else system('cls')

#calculation of volume of cube
def VOL_1():
        system('clear') if platform.system()=='Linux'else system('cls')
        print('Select Operation :- ')
        print('')
        print('1 : Volume of cube')
        print('2 : Side of cube')
        print('3 : Go back  to main menu')
        print('')

        x3=int(input('Select category: '))
        print('')

        if x3==1:
                s=int(input('enter the length of side of the cube: '))
                c=s*s*s
                print('')
                print('The volume of cube is: ',c)
                input('Press Enter to continue ')
                
        elif x3==2:
                c=int(input('enter the volume of the cube'))
                s=c**(1/3)
                print('')
                print('The length of the cube is: ',s)
                input('Press Enter to continue ')
                
        elif x3==3:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid Choice')
                print('')
                sleep(2)
                system('clear') if platform.system()=='Linux'else system('cls')

def VOL_2():
        system('clear') if platform.system()=='Linux'else system('cls')
        print('Select Operation :- ')
        print('')
        print('1: Volume of Cuboid')
        print('2: length of the Cuboid')
        print('3: Breadth of the Cuboid')
        print('4: Height of the Cuboid')
        print('5: Go back to main menu')
        print('')

        x3=int(input('Select Category:  '))
        print('')

        if x3==1:
                l=int(input('enter the length of the Cuboid: '))
                b=int(input('enter the breadth of the Cuboid: '))
                h=int(input('enter the height of the Cuboid: '))
                v=l*b*h
                print('')
                print('the volume of the Cuboid: ',v)
                input('Press Enter to continue ')
                
        elif x3==2:
                b=int(input('enter the breadth of the Cuboid: '))
                h=int(input('enter the height of the Cuboid: '))
                a=int(input('enter the Volume of the Cuboid: '))
                l=a/(b*h)
                print('')
                print('the length of the Cuboid : ',l)
                input('Press Enter to continue ')
                
        elif x3==3:
                l=int(input('enter the length of the Cuboid: '))
                h=int(input('enter the height of the Cuboid: '))
                v=int(input('enter the Volume of the Cuboid: '))
                b=v/(h*l)
                print('')
                print('the breadth of the Cuboid : ',b)
                input('Press Enter to continue ')
                
        elif x3==4:
                l=int(input('enter the length of the Cuboid: '))
                b=int(input('enter the breadth of the Cuboid: '))
                v=int(input('enter the Volume of the Cuboid: '))
                h=v/(b*l)
                print('')
                print('the height of the Cuboid : ',h)
                input('Press Enter to continue ')
                
        elif x3==5:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid Choice')
                print('')
                sleep(2)
                system('clear')if platform.system()=='Linux'else system('cls')
                
def VOL_3():
        system('clear') if platform.system()=='Linux'else system('cls')
        print('Select Operation :- ')
        print('')
        print('1: Volume of Sphere :')
        print('2: Side of the Sphere :')
        print('3: Go back to main menu')
        print('')

        x3=int(input('Select Category: '))
        print('')

        if x3==1:
                r=int(input('enter the radius of the sphere'))
                v=(4/3*3.14)*(r**3)
                print('')
                print('The volume is: ',v)
                input('Press Enter to continue ')
                
        elif x3==2:
                v=int(input('enter the volume of sphere'))
                r=((v*3)/(4*3.14))**(1/3)
                print('')
                print('The radius of the sphere: ',r)
                input('Press Enter to continue ')
                
        elif x3==3:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid choice')
                print('')
                sleep(2)
                system('clear')if platform.system()=='Linux'else system('cls')

def VOL_4():
        system('clear')if platform.system()=='Linux'else system('cls')
        print('Select operation:- ')
        print('')
        print('1: Area of the square :')
        print('2: length of the side of the sqaure')
        print('3: Go back to main menu ')
        print('')

        x2=int(input('Select Category: '))
        print('')

        if x2==1:
                s=int(input('enter the side of the square'))
                a=s*s
                print('')
                print('The area of the sqaure : ',a)
                input('Press Enter to continue ')

        elif x2==2:
                a=int(input('enter the area of square'))
                s=(a)**(1/2)
                print('')
                print('The side of the square : ',s)
                input('Press Enter to continue ')
                
        elif x2==3:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid choice')
                print('')
                sleep(2)
                system('clear')if platform.system()=='Linux'else system('cls')
                
def VOL_5():
        system('clear')if platform.system()=='Linux'else system('cls')
        print('select operetaion:- ')
        print('')
        print('1: Area of the triangle :')
        print('2: base of the trangle')
        print('3: height of triangle')
        print('4: Go back to main menu')
        print('')

        x2=int(input('select Category: '))
        print('')

        if x2==1:
                b=int(input('enter the base of the triangle'))
                h=int(input('enter the height of the triangle'))
                a=(1/2)*b*h
                print('')
                print('The area of the sqaure : ',a)
                input('Press Enter to continue ')

        elif x2==2:
                a=int(input('enter the area of triangle'))
                h=int(input('enter the height of the triangle'))
                s=(2*a)/h
                print('')
                print('The base of the triangle : ',s)
                input('Press Enter to continue ')

        elif x2==3:
                a=int(input('enter the area of triangle'))
                b=int(input('enter the base of the triangle'))
                s=(2*a)/b
                print('')
                print('The height of the triangle is: ',s)
                input('Press Enter to continue ')
                
        elif x2==4:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid choice')
                print('')
                sleep(2)
                system('clear')if platform.system()=='Linux'else system('cls')
                
def VOL_6():
        system('clear')if platform.system()=='Linux'else system('cls')
        print('select operetaion:- ')
        print('')
        print('1: Area of the rectangle :')
        print('2: length of the rectangle')
        print('3: breadth of rectangle')
        print('4: Go back to main')
        print('')

        x2=int(input('select Category: '))
        print('')
        if x2==1:
                l=int(input('enter the length of the rectangle'))
                b=int(input('enter the breadth of the rectangle'))
                a=l*b
                print('')
                print('The area of the sqaure : ',a)
                input('Press Enter to continue ')

        elif x2==2:
                a=int(input('enter the area of rectangle'))
                b=int(input('enter the breadth of the rectangle'))
                m=(a/b)
                print('')
                print('The length of the square',m)
                input('Press Enter to continue ')
                
        elif x2==3: 
                a=int(input('enter the area of rectangle'))
                b=int(input('enter the length of the rectangle'))
                s=a/b
                print('')
                print('The breadth of the square: ',s)
                input('Press Enter to continue ')
                
        elif x2==4:
                system('clear') if platform.system()=='Linux' else system('cls')
                main() 
        else:
                print('Invalid choice')
                print('')
                sleep(2)
                system('clear')if platform.system()=='Linux'else system('cls')
                
#CALCULATION OF CONSUMER FORMULA
def CONS():
        
        
        system('clear') if platform.system()=='Linux'else system('cls')
        print('Formulas :- ')
        print('')
        print('1 : formula for simple interest')
        print('2 : formula of compound interest')
        print('3 : Sales Tax Formula')
        print('4 : Go back to main menu')
        print('')
        
        x2=int(input('Select category: '))

        if x2==1:
                CON_1()
        elif x2==2:
                CON_2()
        elif x2==3:
                CON_3()
        elif x2==4:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid choice !')
                print('')
                sleep(2)
                system('clear') if platform.system()=='Linux'else system('cls')

def CON_1():
        system('clear')if platform.system()=='Linux'else system('cls')
        print('select operetaion:- ')
        print('')
        print('1: To find Simple interest :')
        print('2: TO find the principle amount :')
        print('3: To find the rate of interest: ')
        print('4: To find the time duration : ')
        print('5: Go back to main menu')

        print('')

        x2=int(input('select Category: '))

        if x2==1:
                p=int(input('ener the principal amount'))
                q=int(input('enter the rate of interest'))
                r=int(input('enter the time amount'))
                m=(p*q*r)/100
                print('')
                print('the simple interest is : ',m)
                input('Press Enter to continue ')
                
        elif x2==2:
                m=int(input('enter the simple interest'))
                q=int(input('enter the rate of interest'))
                r=int(input('enter the time amount'))
                p=(m*100)/(q*r)
                print('')
                print('the principle amount is : ',p)
                input('Press Enter to continue ')
                
        elif x2==3:
                m=int(input('enter the simple interest'))
                q=int(input('enter the principle amount'))
                r=int(input('enter the time amount'))
                print('')
                p=(m*100)/(q*r)
                print('the rate of interest is : ',p)
                input('Press Enter to continue ')
                
        elif x2==4:
                m=int(input('enter the simple interest'))
                q=int(input('enter the rate of interest'))
                r=int(input('enter the time amount'))
                print('')
                p=(m*100)/(q*r)
                print('the principle amount is : ',p)
                input('Press Enter to continue ')
                
        elif x2==5:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid choice !')
                print('')
                sleep(2)
                system('clear') if platform.system()=='Linux'else system('cls') 

def CON_2():
        system('clear')if platform.system()=='Linux'else system('cls')
        print('Select operetaion:- ')
        print('')
        print('1: To find Compound interest :')
        print('2: Go back to main menu')
        
        print('')

        x2=int(input('select Category: '))
        print('')

        if x2==1:
                p=int(input('ener the principal amount'))
                q=int(input('enter the rate of interest'))
                r=int(input('enter the time amount'))
                z=int(input('enter the number of times that interest is compounded per unit t '))
                a=p((1+(r/z))**(z*q))
                print('the compound interest is: ',a)
                input('Press Enter to continue ')
                
        elif x2==2:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid choice !')
                print('')
                sleep(2)
                system('clear') if platform.system()=='Linux'else system('cls')
                
def CON_3():
        system('clear')if platform.system()=='Linux'else system('cls')
        print('select operetaion:- ')
        print('')
        print('1: To find Sales tax :')
        print('2: TO find price of item :')
        print('3: TO find the tax rate: ')
        print('4: Go back to main menu')

        print('')

        x2=int(input('select Category: '))
        print('')

        if x2==1:
                p=int(input('enter the price of item'))
                q=int(input('enter the rate of tax'))
                s=p*q
                print('')
                print('The sales tax are: ',s)
                input('Press Enter to continue ')
                
        elif x2==2:
                p=int(input('enter the sales tax of the item'))
                q=int(input('enter the rate of tax'))
                s=p/q
                print('')
                print('The price of the item are: ',s)
                input('Press Enter to continue ')
                
        elif x2==3:
                p=int(input('enter the sales tax of the item'))
                q=int(input('enter the price of the item'))
                s=p/q
                print('')
                print('The rate of tax are :',s)
                input('Press Enter to continue ')
                
        elif x2==4:
                system('clear') if platform.system()=='Linux' else system('cls')
                main()
        else:
                print('Invalid choice !')
                print('')
                sleep(2)
                system('clear') if platform.system()=='Linux'else system('cls')
                
def main():
        system('clear') if platform.system()=='Linux'else system('cls')
        print('Topics:- ')
        print('')
        print('1 = Laws of Motion')
        print('2 = Centroid of plane figure and Surface area')
        print('3 = Reflection')
        print('4 = Volume and Area of plane figures')
        print('5 = Consumer Formulas')
        print('6 = View Credits')
        print('7 = Exit')
        print('')
        x=int(input('Select category: '))
        
        if x==1:
            LAW()
        elif x==2:
            CG()
        elif x==3:
            MIRROR()
        elif x==4:
            VOL()
        elif x==5:
            CONS()
        elif x==6:
            system('clear') if platform.system()=='Linux'else system('cls')
            print('')
            print('')
            print('This program is made by: -')
            print('')
            print('Prajnadeep Das')
            print('Ajoy Kumar Das')
            print('Joseph Kiran Chayengia')
            print('Gitarthi Gogoi')
            print('Sarodi Parasor')
            print('')
            #print('\U0001f600')
            sleep(10)
            main()
        elif x==7:
            exit()
        else:
    
            print('Invalid choice !')
            print('')
            sleep(2)
            system('clear') if platform.system()=='Linux'else system('cls')

#Opening animation
system('clear') if platform.system()=='Linux'else system('cls')
print('Loading [        ]')
sleep(0.5)
system('clear') if platform.system()=='Linux'else system('cls')
print('Loading [.       ]')
sleep(0.5)
system('clear') if platform.system()=='Linux'else system('cls')
print('Loading [..      ]')
sleep(0.5)
system('clear') if platform.system()=='Linux'else system('cls')
print('Loading [...     ]')
sleep(0.5)
system('clear') if platform.system()=='Linux'else system('cls')
print('Loading [....    ]')
sleep(0.2)
system('clear') if platform.system()=='Linux'else system('cls')
print('Loading [.....   ]')
sleep(0.3)
system('clear') if platform.system()=='Linux'else system('cls')
print('Loading [......  ]')
sleep(0.3)
system('clear') if platform.system()=='Linux'else system('cls')
print('Loading [....... ]')
sleep(0.2)
system('clear') if platform.system()=='Linux'else system('cls')
print('Loading [........]')
sleep(0.5)

while 1:
        main()
