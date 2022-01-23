import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SweepFrequencyComponent } from './sweep-frequency.component';

describe('SweepFrequencyComponent', () => {
  let component: SweepFrequencyComponent;
  let fixture: ComponentFixture<SweepFrequencyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SweepFrequencyComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SweepFrequencyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
