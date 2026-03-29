from django.shortcuts import render

# Create your views here.

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Patient
import json

# ── POST: Patient add karo ──────────────────────────────────────
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_patient(request):
    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"status": "Failed", "message": "Invalid JSON"})

    # Required fields check
    REQUIRED = ['patientName', 'gender', 'phoneNumber',
                'dateOfBirth', 'state', 'locality', 'pincode']

    missing = [f for f in REQUIRED if not data.get(f)]
    if missing:
        return JsonResponse({
            "status": "Failed",
            "message": f"{missing} field(s) missing"
        })

    # Patient banao
    patient = Patient.objects.create(
        patient_name  = data['patientName'],
        gender        = data['gender'],
        phone_number  = data['phoneNumber'],
        date_of_birth = data['dateOfBirth'],
        state         = data['state'],
        locality      = data['locality'],
        pincode       = data['pincode'],
        email         = data.get('emailId', ''),
        address       = data.get('address', ''),
        city          = data.get('city', ''),
        aadhaar_no    = data.get('aadhaarCard', ''),
        height        = data.get('height', ''),
        weight        = data.get('weight', ''),
    )

    return JsonResponse({
        "status": "Success",
        "message": "Patient registered successfully",
        "patient_id": patient.id
    })


# ── GET: Patient fetch karo by ID ───────────────────────────────
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_patient(request, patient_id):
    try:
        p = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return JsonResponse({"status": "Failed", "message": "Patient not found"})

    return JsonResponse({
        "status": "Success",
        "data": {
            "patientName":  p.patient_name,
            "gender":       p.gender,
            "phoneNumber":  p.phone_number,
            "dateOfBirth":  str(p.date_of_birth),
            "state":        p.state,
            "locality":     p.locality,
            "pincode":      p.pincode,
            "emailId":      p.email,
            "address":      p.address,
            "city":         p.city,
            "aadhaarCard":  p.aadhaar_no,
            "height":       p.height,
            "weight":       p.weight,
            "createdAt":    str(p.created_at),
        }
    })


# ── GET: Sare patients list ─────────────────────────────────────
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_patients(request):
    patients = Patient.objects.all().order_by('-created_at')
    data = []
    for p in patients:
        data.append({
            "id":           p.id,
            "patientName":  p.patient_name,
            "gender":       p.gender,
            "phoneNumber":  p.phone_number,
            "dateOfBirth":  str(p.date_of_birth),
        })
    return JsonResponse({"status": "Success", "data": data})