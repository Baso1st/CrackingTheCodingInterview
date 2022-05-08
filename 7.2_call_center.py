"""
#### NOTE this system should be desingend asynchronous instead of what's done below. ### 
# 3 differenty types of employess: respondent, manager, and director,
# A DispatchCall() method is our starting point. 
# We probably have multiple respondents
# Possible classes: CallCenter, Employee, Respondent, Manager, Director, Call
# The call center will have a list of respondent, a list of managers and a list of directors
    It will also have the dispatchCall() Method and the MonitorCalls() Method
# We create an instance of the CallCenter,
    Assign it some respondent, managers and directors.
    The MonitorCalls Method will start running immediately.
    The call center will have 3 queues for each call type
    The dispatchCall() Will add a call to the low priority queue 
    The MonitorCalls() Method will take calls from the queues and assign them to employees based on the levels.
    If no respondent is available it will keep looping until one is available
    Once a respondent is assigned, the respondent takeCall() Method will have a random check to decide if the respondent
        can or can't handle the call. 
        if the respondent can't handle the call it will place it in the next level queue.
    Once a call is dealt with it will be added to a finished Calls list.
"""

from abc import ABC, abstractmethod
from multiprocessing.connection import wait
from random import randint
import time


class Call():
    def __init__(self, caller: str) -> None:
        self.caller = caller


class Employee(ABC):
    def __init__(self, name) -> None:
        super().__init__()
        self.available = True
        self.name = name

    @abstractmethod
    def take_call(self, call: Call):
        self.available = False


class Respondent(Employee):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def take_call(self, call: Call):
        super().take_call(call)
        canHandleTheCall = randint(0, 4) # Respondents can handle 80% of the calls they recieve.
        isTakenCareOf = False
        time.sleep(0.1)
        if canHandleTheCall:
            time.sleep(0.5)
            isTakenCareOf = True
        else:
            isTakenCareOf = False
        
        self.available = True
        return isTakenCareOf


class Manager(Employee):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def take_call(self, call: Call):
        super().take_call(call)
        canHandleTheCall = randint(0, 2) # Managers can handle 66.67% of the calls escalted to them.
        isTakenCareOf = False
        time.sleep(0.1)
        if canHandleTheCall:
            time.sleep(0.5)
            isTakenCareOf = True
        else:
            isTakenCareOf = False
        
        self.available = True
        return isTakenCareOf


class Director(Employee):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def take_call(self, call: Call):
        super().take_call(call)
        time.sleep(0.5)
        self.available = True
        return True


class CallCenter():
    def __init__(self, employees, calls) -> None:
        self._respondents = []
        self._managers = []
        self._directors = []
        self._respondentCalls = []
        self._managerCalls = []
        self._directorCalls = []
        self._finishedCalls = []
        for employee in employees:
            if type(employee) == Respondent:
                self._respondents.append(employee)
            elif type(employee) == Manager:
                self._managers.append(employee)
            elif type(employee) == Director:
                self._directors.append(employee)
            else:
                raise Exception("Unknown Employee Type")

        self._respondentCalls = calls

    def dispatch_call(self):
        while True:
            if self._directorCalls and self._directors:
                call = self._directorCalls.pop(0)
                self._take_director_call(call)

            if self._managerCalls:
                if self._managers:
                    manager = self._managers.pop(0)
                    call = self._managerCalls.pop(0)
                    callIsTakenCareOf = manager.take_call(call)
                    self._managers.append(manager)
                    if callIsTakenCareOf:
                        self._finish_call(call, manager)
                    else:
                        self._directorCalls.append(call)

                elif self._directors: # If no Manager available, then send it to a director.
                    call = self._managerCalls.pop(0)
                    self._take_director_call(call)
            
            if self._respondentCalls and self._respondents:
                call = self._respondentCalls.pop(0)
                respondent = self._respondents.pop(0)
                callIsTakenCareOf = respondent.take_call(call)
 
                if callIsTakenCareOf:
                    self._finish_call(call, respondent)
                else:
                    self._managerCalls.append(call)
    
                self._respondents.append(respondent)

            # time.sleep(1)

    
    def _take_director_call(self, call):
        if self._directors:
            director = self._directors.pop(0)
            if director.available:
                director.take_call(call)
                self._directors.append(director)
                self._finish_call(call, director)
    
    def _finish_call(self, call, employee: Employee):
        self._finishedCalls.append(call)
        print(f"{call.caller} handled by {employee.name}")


def main():
    respondents = []
    managers = []
    directors = []

    for i in range(20):
        res = Respondent(f"Respondent {i}")
        respondents.append(res)

    for i in range(5):
        manager = Manager(f"Manager {i}")
        managers.append(manager)

    for i in range(2):
        director = Director(f"Director {i}")
        directors.append(director)
    
    employees = respondents + managers + directors

    calls = []
    for i in range(1000):
        call = Call(f"Caller {i}")
        calls.append(call)

    callCenter = CallCenter(employees, calls)
    callCenter.dispatch_call()


if __name__ == '__main__':
    main()