@echo off
rem Swipe-file pull. Fill in the three paths, save it where you can double-click it.
powershell -NoProfile -ExecutionPolicy Bypass -File "<path to skills>\swipe-file\tools\swipe_pull.ps1" -Drop "<drop folder>" -Out "<work folder>"
