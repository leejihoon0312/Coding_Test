def solution(cap, n, deliveries, pickups):
    answer = 0

    delivered = 0
    pickuped = 0

    for idx in range(1, n + 1):
        while deliveries[-idx] != 0 or pickups[-idx] != 0:
            if delivered - deliveries[-idx] < 0:
                deliveries[-idx] -= delivered
                delivered = 0
            else:
                delivered = delivered - deliveries[-idx]
                deliveries[-idx] = 0

            if pickuped - pickups[-idx] < 0:
                pickups[-idx] -= pickuped
                pickuped = 0
            else:
                pickuped = pickuped - pickups[-idx]
                pickups[-idx] = 0

            if deliveries[-idx] > 0 or pickups[-idx] > 0:
                answer += (n - idx + 1) * 2

                if cap - deliveries[-idx] >= 0:
                    delivered += cap - deliveries[-idx]
                    deliveries[-idx] = 0
                else:
                    deliveries[-idx] -= cap
                    delivered = 0

                if cap - pickups[-idx] >= 0:
                    pickuped += cap - pickups[-idx]
                    pickups[-idx] = 0
                else:
                    pickups[-idx] -= cap
                    pickuped = 0
    return answer