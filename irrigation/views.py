from django.shortcuts import render
from .models import SensorData, IrrigationSchedule
from django.utils import timezone
from django.http import HttpResponse

def irrigation_control(request):
    context = {}
    
    try:
        # Try to fetch the latest sensor data
        latest_data = SensorData.objects.latest('timestamp')
        context['latest_data'] = latest_data

        # Irrigation logic based on sensor data
        if latest_data.soil_moisture < 30:  # Threshold moisture level
            # Schedule irrigation
            start_time = timezone.now()
            end_time = start_time + timezone.timedelta(minutes=15)
            water_amount = 10  # e.g., 10 liters of water
            
            # Save the schedule to the database
            irrigation = IrrigationSchedule.objects.create(
                start_time=start_time,
                end_time=end_time,
                water_amount=water_amount
            )
            context['irrigation'] = irrigation
            context['message'] = "Irrigation started!"
        else:
            context['message'] = "No irrigation needed!"
        
    except SensorData.DoesNotExist:
        # If no sensor data exists, handle the case gracefully
        context['message'] = "No sensor data available. Please add sensor data first."
    
    return render(request, 'irrigation/control.html', context)




from django.shortcuts import render
from .models import SensorData, IrrigationSchedule
from django.utils import timezone

def dashboard(request):
    # Get the latest sensor data
    try:
        latest_sensor_data = SensorData.objects.latest('timestamp')
    except SensorData.DoesNotExist:
        latest_sensor_data = None

    # Get recent irrigation events (e.g., last 7 days)
    recent_events = IrrigationSchedule.objects.filter(
        start_time__gte=timezone.now() - timezone.timedelta(days=7)
    ).order_by('-start_time')

    # Context data to pass to the template
    context = {
        'latest_sensor_data': latest_sensor_data,
        'recent_events': recent_events
    }

    return render(request, 'dashboard.html', context)
















from .models import IrrigationSchedule

def irrigation_history(request):
    # Retrieve all irrigation schedules
    schedules = IrrigationSchedule.objects.all()
    
    # Pass schedules to the template
    return render(request, 'irrigation/history.html', {'schedules': schedules})