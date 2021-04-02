
class Event_event_bus():
    def __init__(self):
        self.__listeners = {}

    def subscribe(self, event_type, method):
        """
        Оформление подписки метода method на событие event_type.
        """ 
        if event_type not in self.__listeners.keys():
            self.__listeners[event_type] = [method]
        else:
            self.__listeners[event_type].append(method)

    def raise_event(self, event_type, *data):
        """
        Вызов события и всего его слушаателей, соответсвено.
        """
        if event_type in self.__listeners.keys():
            for method in self.__listeners[event_type]:
                method(*data)

    def unsubscribe(self, event_type, method):
        """
        Отмена подписки метода method на событие event_type.
        """
        if event_type in self.__listeners.keys():
            self.__listeners[event_type].remove(method)
            if len(self.__listeners[event_type]) == 0:
                del self.__listeners[event_type]

def raise_all(event_bus):
    print()
    event_bus.raise_event("event_1", "#1")
    event_bus.raise_event("event_2", "#2")

if __name__ == '__main__':
    event_bus = Event_event_bus()
    method1 = lambda x: print("call_1: " + x)
    method2 = lambda x: print("call_2: " + x)

    event_bus.subscribe("event_1", method1)
    event_bus.subscribe("event_1", method2)
    event_bus.subscribe("event_2", method1)

    raise_all(event_bus)

    event_bus.unsubscribe("event_1", method2)
    raise_all(event_bus)