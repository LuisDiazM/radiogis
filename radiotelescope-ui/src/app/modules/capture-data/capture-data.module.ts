import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CaptureDataRoutingModule } from './capture-data-routing.module';
import { SingleFrequencyComponent } from './pages/single-frequency/single-frequency.component';
import { SweepFrequencyComponent } from './pages/sweep-frequency/sweep-frequency.component';
import { PrimengModule } from '../../primeng.module';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [SingleFrequencyComponent, SweepFrequencyComponent],
  imports: [
    CommonModule,
    CaptureDataRoutingModule,
    PrimengModule,
    FormsModule,
  ],
})
export class CaptureDataModule {}
