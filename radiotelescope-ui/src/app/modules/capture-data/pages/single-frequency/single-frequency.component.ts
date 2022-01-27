import { Component, OnInit } from '@angular/core';
import { FFTModel } from '../../models/captureData.model';

@Component({
  selector: 'app-single-frequency',
  templateUrl: './single-frequency.component.html',
  styleUrls: ['./single-frequency.component.css'],
})
export class SingleFrequencyComponent implements OnInit {
  MAX_ELEVATION: number = 180;
  MAX_BW: number = 20e6;
  MAX_AZIMUT: number = 360;
  nfft!: FFTModel[];

  fftSize!: FFTModel;
  frequency: number = 100e6; //Hz
  azimut: number = 0;
  elevation: number = 0;
  bw: number = 1e6;
  timer: number = 1

  constructor() {}

  ngOnInit(): void {
    this.nfft = [{ fft: 1024 }, { fft: 2048 }, { fft: 4096 }];
  }
}
