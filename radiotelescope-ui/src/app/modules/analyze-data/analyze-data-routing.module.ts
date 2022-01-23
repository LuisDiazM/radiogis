import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SpectrumComponent } from './pages/spectrum/spectrum.component';
import { DataRawComponent } from './pages/data-raw/data-raw.component';

const routes: Routes = [
  {
    path: '',
    children: [
      { path: 'spectrum', component: SpectrumComponent },
      { path: 'data-raw', component: DataRawComponent },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class AnalyzeDataRoutingModule {}
