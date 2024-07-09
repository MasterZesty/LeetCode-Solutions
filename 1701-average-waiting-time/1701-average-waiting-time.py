class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        time_passed = customers[0][0] # start global clock at first customer
        avg_waiting_time = 0
        no_customers = len(customers)
        
        for i, customer in enumerate(customers):
            
            arrival_time = customer[0]
            order_prepare_time = customer[1]
            
            # Calculate the actual start time for the current customer
            start_time = max(time_passed, arrival_time)
            
            current_customer_waiting_time = start_time - arrival_time + order_prepare_time
                
            avg_waiting_time += current_customer_waiting_time
            
            time_passed = start_time + order_prepare_time
            
            # print(f"customer: {i+1} |customer t: {customer} | current waiting t: {current_customer_waiting_time} | time_passed: {time_passed}")
        
        # print(f"avg_waiting_time: {avg_waiting_time} | {avg_waiting_time/no_customers}")
        return avg_waiting_time/no_customers