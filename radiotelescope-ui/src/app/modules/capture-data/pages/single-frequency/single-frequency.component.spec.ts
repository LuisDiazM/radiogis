import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SingleFrequencyComponent } from './single-frequency.component';

describe('SingleFrequencyComponent', () => {
  let component: SingleFrequencyComponent;
  let fixture: ComponentFixture<SingleFrequencyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SingleFrequencyComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SingleFrequencyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
