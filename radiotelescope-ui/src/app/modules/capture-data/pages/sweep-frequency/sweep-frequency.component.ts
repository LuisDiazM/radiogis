import { Component, OnInit } from '@angular/core';
import { ConfirmationService } from 'primeng/api';
import { BWFrequencies, FFTModel } from '../../models/captureData.model';

@Component({
  selector: 'app-sweep-frequency',
  templateUrl: './sweep-frequency.component.html',
  styleUrls: ['./sweep-frequency.component.css']
})
export class SweepFrequencyComponent implements OnInit {

  MAX_ELEVATION: number = 180;
  MAX_BW: number = 20e6;
  MAX_AZIMUT: number = 360;
  nfft!: FFTModel[];
  frequencySample!: BWFrequencies[];
  fftSize: FFTModel = { fft: 1024 };

  frequency: number[] = [100, 200];
  BWFreq: BWFrequencies = { sampleFrequency: 16e6 }; //Hz
  azimut: number = 0;
  elevation: number = 0;
  bw: number = 1e6;
  timer: number = 1;

  constructor(private confirmationService: ConfirmationService) {}

  ngOnInit(): void {
    this.nfft = [{ fft: 1024 }, { fft: 2048 }, { fft: 4096 }];
    this.frequencySample = [
      { sampleFrequency: 20e6 },
      { sampleFrequency: 16e6 },
      { sampleFrequency: 8e6 },
      { sampleFrequency: 4e6 },
      { sampleFrequency: 2e6 },
      { sampleFrequency: 1e6 },
      { sampleFrequency: 500e3 },
    ];
  }

  confirm() {
    this.confirmationService.confirm({
      message: `(BW ${this.BWFreq?.sampleFrequency}), (Frecuencia central ${this.frequency}) \n
      (FFT ${this.fftSize?.fft}) (azimut ${this.azimut}) (elevacion ${this.elevation})`,
      header: '¿Está seguro tomar datos con los siguientes parámetros?',
      acceptLabel: "Si",
      rejectLabel: "No",
      accept: () => {
        //Actual logic to perform a confirmation
      },
    });
  }

}
