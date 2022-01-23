import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainInfoComponent } from './shared/main-info/main-info.component';

const routes: Routes = [
  { path: '', component: MainInfoComponent },
  {
    path: 'capture-data',
    loadChildren: () =>
      import('./modules/capture-data/capture-data.module').then(
        (m) => m.CaptureDataModule
      ),
  },
  {
    path: 'analyze-data',
    loadChildren: () =>
      import('./modules/analyze-data/analyze-data.module').then(
        (m) => m.AnalyzeDataModule
      ),
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
