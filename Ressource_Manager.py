class ResourceManager:
    @staticmethod
    def modify_resource_amount(resources, resource_type, amount):
        resources[resource_type] += amount