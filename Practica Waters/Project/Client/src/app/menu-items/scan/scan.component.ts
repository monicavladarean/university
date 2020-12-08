import { Component, OnInit } from '@angular/core';
import {BarcodeFormat} from '@zxing/library';
import {Router} from '@angular/router';

@Component({
  selector: 'app-scan',
  templateUrl: './scan.component.html',
  styleUrls: ['./scan.component.css']
})
export class ScanComponent implements OnInit {

  torchEnabled = false;
  tryHarder = false;
  currentDevice = MediaDeviceInfo = null;
  formats = [BarcodeFormat.QR_CODE]; 
  availableDecive: MediaDeviceInfo[];
  hasPermission: boolean;
  constructor(private router:Router) { }

  ngOnInit(): void {
  }


  onHasPermission(permission:boolean){
    this.hasPermission = permission;
    console.log('Camera permission: ' + permission);
  }

  onCamerasFound(devices: MediaDeviceInfo[]){
    this.availableDecive = devices;
    devices.forEach((camera) =>
    console.log('Camera: ' + camera.label));
  }

  onScanSuccess(data: string){
    console.log('Data from QR' + data);
    this.router.navigate(['/item/' + data]);
  }

}
