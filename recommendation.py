import random

users = ["user1", "user2", "user3", "user4"]
items = ["item1", "item2", "item3", "item4", "item5", "item6"]
purchases_history = {
    "user1": [["item1", "item2", "item3"], ["item1", "item2", "item4"]],
    "user2": [["item2", "item5"], ["item4", "item5"]],
    "user3": [["item3", "item2"]],
    "user4": []
}

def get_user_stats(user, items, history):
    stats = {}
    for item in items:
        stats[item] = []
        for purchase in history:
            if item in purchase:
                for other_item in purchase:
                    if other_item != item:
                        stats[item].append(other_item)
    return stats

def get_all_users_stats(purchases_history):
    all_users_stats = {}
    for user, history in purchases_history.items():
        all_users_stats[user] = get_user_stats(user, items, history)
    return all_users_stats

def freq_list_users(user, all_users_stats):
    user_stats = all_users_stats.get(user, {})
    freq = {}
    for item, related_items in user_stats.items():
        for related_item in related_items:
            if related_item in freq:
                freq[related_item] += 1
            else:
                freq[related_item] = 1
    return freq

def recommend_based_on_users(user, all_users_stats):
    freq = freq_list_users(user, all_users_stats)
    if freq:
        max_freq = max(freq.values())
        recommendations = [item for item, count in freq.items() if count == max_freq]
        return random.choice(recommendations)
    return None

def recommend(user, cart, all_users_stats):
    user_recommendation = recommend_based_on_users(user, all_users_stats)
    item_recommendation = recommend_based_on_items_in_cart(user, cart, all_users_stats)
    if user_recommendation and item_recommendation:
        return random.choice([user_recommendation, item_recommendation])
    elif user_recommendation:
        return user_recommendation
    elif item_recommendation:
        return item_recommendation
    else:
        return random.choice(items)

def freq_list_items(user, all_users_stats):
    user_stats = all_users_stats.get(user, {})
    freq = {}
    for item, related_items in user_stats.items():
        freq[item] = len(related_items)
    return freq

def freq_list_cart(user, cart, all_users_stats):
    user_stats = all_users_stats.get(user, {})
    freq = {}
    for cart_item in cart:
        for item, related_items in user_stats.items():
            if cart_item in related_items and item not in cart:
                if item in freq:
                    freq[item] += 1
                else:
                    freq[item] = 1
    return freq

def freq_list_cart_and_items(user, cart, all_users_stats):
    freq_items = freq_list_items(user, all_users_stats)
    freq_cart = freq_list_cart(user, cart, all_users_stats)
    combined_freq = {**freq_items, **freq_cart}
    for item in combined_freq:
        if item in freq_items and item in freq_cart:
            combined_freq[item] = freq_items[item] + freq_cart[item]
    return combined_freq

def recommend_based_on_items_in_cart(user, cart, all_users_stats):
    freq = freq_list_cart_and_items(user, cart, all_users_stats)
    if freq:
        max_freq = max(freq.values())
        recommendations = [item for item, count in freq.items() if count == max_freq]
        return random.choice(recommendations)
    return None

all_users_stats = get_all_users_stats(purchases_history)
