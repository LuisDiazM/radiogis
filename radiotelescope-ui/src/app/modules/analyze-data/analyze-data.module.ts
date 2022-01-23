import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AnalyzeDataRoutingModule } from './analyze-data-routing.module';
import { SpectrumComponent } from './pages/spectrum/spectrum.component';
import { DataRawComponent } from './pages/data-raw/data-raw.component';


@NgModule({
  declarations: [
    SpectrumComponent,
    DataRawComponent
  ],
  imports: [
    CommonModule,
    AnalyzeDataRoutingModule
  ]
})
export class AnalyzeDataModule { }
