import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SingleFrequencyComponent } from './pages/single-frequency/single-frequency.component';
import { SweepFrequencyComponent } from './pages/sweep-frequency/sweep-frequency.component';

const routes: Routes = [
  {
    path:"",
    children: [
      { path: 'single-frequency', component: SingleFrequencyComponent },
      { path: 'sweep-frequency', component: SweepFrequencyComponent },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class CaptureDataRoutingModule {}
