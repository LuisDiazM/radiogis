import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CaptureDataRoutingModule } from './capture-data-routing.module';
import { SingleFrequencyComponent } from './pages/single-frequency/single-frequency.component';
import { SweepFrequencyComponent } from './pages/sweep-frequency/sweep-frequency.component';


@NgModule({
  declarations: [
    SingleFrequencyComponent,
    SweepFrequencyComponent
  ],
  imports: [
    CommonModule,
    CaptureDataRoutingModule
  ]
})
export class CaptureDataModule { }
