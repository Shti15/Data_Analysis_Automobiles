import pandas as pd
import numpy as np
import os


def cleaning():
    df=pd.read_csv(os.getcwd()+"\static\\cars_engage_2022.csv")
    
    nans_indices = df.columns[df.isna().any()].tolist()
    # to-do: make,doors 
    #make


    #displacement
    df.drop(df.index[(df['Displacement']).isna()], inplace=True)
    print(df.isnull().sum(axis = 0))
    print(df)

    #cylinders
    (df['Cylinders']).fillna(value="Unknown", inplace=True)

    #Valves_per_cylinder
    df.drop(['Valves_Per_Cylinder'], axis = 1)

    #Drivetrain
    df.drop(df.index[(df['Drivetrain']).isna()], inplace=True)

    #Cylinder_Configuration
    df.drop(df.index[(df['Cylinder_Configuration']).isna()], inplace=True)

    #emission norm
    (df['Emission_Norm']).fillna(value="NA", inplace=True)

    #engine location
    df.drop(['Engine_Location'], axis = 1)

    #fuel_system
    (df['Fuel_System']).fillna(value="NA", inplace=True)

    #fuel tank capacity
    (df['Fuel_Tank_Capacity']).fillna(value="NA", inplace=True)

    #height
    df.drop(df.index[(df['Height']).isna()], inplace=True)

    #width
    df.drop(df.index[(df['Width']).isna()], inplace=True)

    #body type
    df.drop(df.index[(df['Body_Type']).isna()], inplace=True)

    #doors
    df.drop(['Doors'], axis = 1)

    #city-mileage
    (df['City_Mileage']).fillna(value="Unknown", inplace=True)

    #Highway mileage
    (df['Highway_Mileage']).fillna(value="Unknown", inplace=True)

    #ARAI certified mileage
    (df['ARAI_Certified_Mileage']).fillna(value="Unknown", inplace=True)

    #Arai cng
    df.drop(['ARAI_Certified_Mileage_for_CNG'], axis = 1)

    #Kerb Weight
    (df['Kerb_Weight']).fillna(value="Unknown", inplace=True)

    #Gears
    (df['Gears']).fillna(value="Unknown", inplace=True)

    #Ground_Clearance
    (df['Ground_Clearance']).fillna(value="Unknown", inplace=True)

    #Front Brakes
    df.drop(df.index[(df['Front_Brakes']).isna()], inplace=True)

    #Rear_Brakes
    df.drop(df.index[(df['Rear_Brakes']).isna()], inplace=True)

    #Front suspension
    df.drop(['Front_Suspension'], axis = 1)

    #Rear suspension
    df.drop(['Rear_Suspension'], axis = 1)

    #Front track
    df.drop(['Front_Track'], axis = 1)

    #Rear track
    df.drop(['Rear_Track'], axis = 1)

    #Front tyre and rim
    df.drop(['Front_Tyre_&_Rim'], axis = 1)

    #rear tyre and rim
    df.drop(['Rear_Tyre_&_Rim'], axis = 1)

    #power steering
    (df['Power_Steering']).fillna(value="Electric", inplace=True)

    #Power windows
    df.drop(['Power_Windows'], axis = 1)
    #power seats 
    df.drop(['Power_Seats'], axis = 1)

    #Keyless_Entry  
    (df['Keyless_Entry']).fillna(value="NA", inplace=True)

    #Torque 
    df.drop(df.index[(df['Torque']).isna()], inplace=True)

    #Odometer, Speedometer,Tachometer, Tripmeter 
    df.drop(['Odometer','Speedometer','Tachometer','Tripmeter'], axis = 1)

    #Seating_Capacity,Seats_Material,Type  ,Wheelbase,Wheels_Size,Start_/_Stop_Button,12v_Power_Outlet 
    df.drop(['Seating_Capacity','Seats_Material','Type','Wheelbase','Wheels_Size','Start_/_Stop_Button','12v_Power_Outlet'], axis = 1)

    #Audiosystem,'Aux-in_Compatibility' ,'Average_Fuel_Consumption' ,
    df.drop(['Audiosystem','Aux-in_Compatibility' ,'Average_Fuel_Consumption'], axis = 1)
    
    #Basic_Warranty
    (df['Basic_Warranty']).fillna(value="NA", inplace=True)

    #Bluetooth
    (df['Bluetooth']).fillna(value="NA", inplace=True)

    #Central_Locking
    (df['Central_Locking']).fillna(value="NA", inplace=True)

    #Child_Safety_Locks 
    df.drop(['Child_Safety_Locks'], axis = 1)

    #Clock
    (df['Clock']).fillna(value="digital", inplace=True)

    #Cup_Holders ,Distance_to_Empty,Door_Pockets,Engine_Malfunction_Light 
    df.drop(['Cup_Holders' ,'Distance_to_Empty','Door_Pockets','Engine_Malfunction_Light'], axis = 1)

    #Extended_Warranty
    (df['Extended_Warranty']).fillna(value="NA", inplace=True)

    #FM_Radio,Fuel-lid_Opener
    df.drop(['FM_Radio','Fuel-lid_Opener'], axis = 1)

    #Fuel_Gauge
    df.drop(['Fuel_Gauge'], axis = 1)

    # Handbrake
    df.drop(['Handbrake'], axis = 1)

    # Instrument_Console 
    df.drop(['Instrument_Console'], axis = 1)

    #Low_Fuel_Warning
    df.drop(['Low_Fuel_Warning'], axis = 1)

    # Minimum_Turning_Radius
    df.drop(['Minimum_Turning_Radius'], axis = 1)

    # Multifunction_Display
    df.drop(['Multifunction_Display'], axis = 1)

    # Sun_Visor
    df.drop(['Sun_Visor'], axis = 1)

    #Third_Row_AC_Vents 
    df.drop(['Third_Row_AC_Vents'], axis = 1)

    # Ventilation_System
    df.drop(['Ventilation_System'], axis = 1)

    # Auto-Dimming_Rear-View_Mirror
    df.drop(['Auto-Dimming_Rear-View_Mirror'], axis = 1)

    # Hill_Assist  
    df.drop(['Hill_Assist'], axis = 1)

    #Gear_Indicator
    df.drop(['Gear_Indicator'], axis = 1)

    # 3_Point_Seat-Belt_in_Middle_Rear_Seat 
    df.drop(['3_Point_Seat-Belt_in_Middle_Rear_Seat'], axis = 1)

    # Ambient_Lightning
    df.drop(['Ambient_Lightning'], axis = 1)

    #Cargo/Boot_Lights,Drive_Modes 
    df.drop(['Cargo/Boot_Lights','Drive_Modes'], axis = 1)

    # Engine_Immobilizer
    df.drop(['Engine_Immobilizer'], axis = 1)

    #High_Speed_Alert_System
    df.drop(['High_Speed_Alert_System'], axis = 1)
    #Lane_Watch_Camera/_Side_Mirror_Camera
    df.drop(['Lane_Watch_Camera/_Side_Mirror_Camera'], axis = 1)
    #Passenger_Side_Seat-Belt_Reminder  
    df.drop(['Passenger_Side_Seat-Belt_Reminder'], axis = 1)
    #Seat_Back_Pockets
    df.drop(['Seat_Back_Pockets'], axis = 1)
    # Voice_Recognition 
    df.drop(['Voice_Recognition'], axis = 1)
    #Walk_Away_Auto_Car_Lock 
    df.drop(['Walk_Away_Auto_Car_Lock'], axis = 1)
    #ABS_(Anti-lock_Braking_System)
    df.drop(['ABS_(Anti-lock_Braking_System)'], axis = 1)
    #Headlight_Reminder
    df.drop(['Headlight_Reminder'], axis = 1)
    #Adjustable_Headrests
    df.drop(['Adjustable_Headrests'], axis = 1)

    #Gross_Vehicle_Weight 
    (df['Gross_Vehicle_Weight']).fillna(value="NA", inplace=True)

    #Airbags     
    df.drop(['Airbags'], axis = 1)
    #Door_Ajar_Warning     
    df.drop(['Door_Ajar_Warning'], axis = 1)
    #EBD_(Electronic_Brake-force_Distribution)
    df.drop(['EBD_(Electronic_Brake-force_Distribution)'], axis = 1)    
    #Fasten_Seat_Belt_Warning    
    df.drop(['Fasten_Seat_Belt_Warning'], axis = 1)
    #Gear_Shift_Reminder     
    df.drop(['Gear_Shift_Reminder'], axis = 1)
    #Number_of_Airbags     
    df.drop(['Number_of_Airbags'], axis = 1)
    #Compression_Ratio    
    df.drop(['Compression_Ratio'], axis = 1)
    #Adjustable_Steering_Column    
    df.drop(['Adjustable_Steering_Column'], axis = 1)
    #Other_Specs         
    df.drop(['Other_Specs'], axis = 1)

    #Parking_Assistance
    (df['Parking_Assistance']).fillna(value="NA", inplace=True)

    #Key_Off_Reminder     
    df.drop(['Key_Off_Reminder'], axis = 1)
    #USB_Compatibility   
    df.drop(['USB_Compatibility'], axis = 1)
    #Android_Auto     
    df.drop(['Android_Auto'], axis = 1)
    #Apple_CarPlay     
    df.drop(['Apple_CarPlay'], axis = 1)
    #Cigarette_Lighter     
    df.drop(['Cigarette_Lighter'], axis = 1)
    #Infotainment_Screen    
    df.drop(['Infotainment_Screen'], axis = 1)
    #Multifunction_Steering_Wheel     
    df.drop(['Multifunction_Steering_Wheel'], axis = 1)
    

    #Average_Speed
    (df['Average_Speed']).fillna(value="NA", inplace=True)

    #EBA_(Electronic_Brake_Assist)     
    df.drop(['EBA_(Electronic_Brake_Assist)'], axis = 1)
    #Seat_Height_Adjustment     
    df.drop(['Seat_Height_Adjustment'], axis = 1)
    #Navigation_System     
    df.drop(['Navigation_System'], axis = 1)
    #Second_Row_AC_Vents     
    df.drop(['Second_Row_AC_Vents'], axis = 1)
    #Tyre_Pressure_Monitoring_System    
    df.drop(['Tyre_Pressure_Monitoring_System'], axis = 1)
    #Rear_Center_Armrest     
    df.drop(['Rear_Center_Armrest'], axis = 1)
    #iPod_Compatibility    
    df.drop(['iPod_Compatibility'], axis = 1)
    #ESP_(Electronic_Stability_Program)   
    df.drop(['ESP_(Electronic_Stability_Program)'], axis = 1)
    #Cooled_Glove_Box     
    df.drop(['Cooled_Glove_Box'], axis = 1)
    #Recommended_Tyre_Pressure     
    df.drop(['Recommended_Tyre_Pressure'], axis = 1)
    #Heated_Seats     
    df.drop(['Heated_Seats'], axis = 1)
    #Turbocharger     
    df.drop(['Turbocharger'], axis = 1)
    #ISOFIX_(Child-Seat_Mount)     
    df.drop(['ISOFIX_(Child-Seat_Mount)'], axis = 1)
    #Rain_Sensing_Wipers     
    df.drop(['Rain_Sensing_Wipers'], axis = 1)
    #Paddle_Shifters     
    df.drop(['Paddle_Shifters'], axis = 1)
    #Leather_Wrapped_Steering     
    df.drop(['Leather_Wrapped_Steering'], axis = 1)
    #Automatic_Headlamps     
    df.drop(['Automatic_Headlamps'], axis = 1)
    #Engine_Type     
    df.drop(['Engine_Type'], axis = 1)
    #ASR_/_Traction_Control    
    df.drop(['ASR_/_Traction_Control'], axis = 1)
    #Cruise_Control     
    df.drop(['Cruise_Control'], axis = 1)
    #USB_Ports     
    df.drop(['USB_Ports'], axis = 1)
    #Heads-Up_Display     
    df.drop(['Heads-Up_Display'], axis = 1)
    #Welcome_Lights    
    df.drop(['Welcome_Lights'], axis = 1)
    #Battery     
    df.drop(['Battery'], axis = 1)

    #Electric_Range     
    df.drop(['Electric_Range'], axis = 1)
    
    df.to_csv(os.getcwd()+'\static\\Clean_data_4w.csv', index=False)

if __name__=='__main__':
    cleaning()