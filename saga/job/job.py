
from saga.Object      import Object
from saga.Task        import Async 
from saga.Permissions import Permissions
from saga.Attributes  import Attributes

class Job (Object, Async, Attributes, Permissions) :
    
    def __init__(self):
    
        # set attribute interface properties
        self.attributes_extensible_  (False)
        self.attributes_camelcasing_ (True)

        # register properties with the attribute interface 
        self.attributes_register_   ('State',      self.Unknown, self.Enum,   self.Scalar, self.ReadOnly)
        self.attributes_register_   ('Exitcode',   None,         self.Int,    self.Scalar, self.ReadOnly)
        self.attributes_register_   ('JobID',      None,         self.String, self.Scalar, self.ReadOnly)
        self.attributes_register_   ('ServiceURL', None,         self.Url,    self.Scalar, self.ReadOnly)

        self.attributes_set_enums_  ('State',   [UNKNOWN, NEW, RUNNING, DONE,
                                                 FAILED,  CANCELED, SUSPENDED])
        
        self.attributes_set_getter_ ('State',    self.get_state)
        self.attributes_set_getter_ ('jobID',    self.get_job_id)
        self.attributes_set_getter_ ('Exitcode', self.get_exitcode_)


    def get_description (self,         ttype=None)           : pass 
    #   ttype:     saga.task.type enum
    #   ret:       saga.job.Description / saga.Task          

    def get_stdin  (self,              ttype=None)           : pass 
    #   ttype:     saga.task.type enum
    #   ret:       os.File / saga.Task

    def get_stdout (self,              ttype=None)           : pass 
    #   ttype:     saga.task.type enum
    #   ret:       os.File / saga.Task

    def get_stderr (self,              ttype=None)           : pass 
    #   ttype:     saga.task.type enum
    #   ret:       os.File / saga.Task

    def suspend    (self,              ttype=None)           : pass 
    #   ttype:     saga.task.type enum
    #   ret:       None / saga.Task

    def resume     (self,              ttype=None)           : pass 
    #   ttype:     saga.task.type enum
    #   ret:       None / saga.Task

    def checkpoint (self,              ttype=None)           : pass 
    #   ttype:     saga.task.type enum
    #   ret:       None / saga.Task

    def migrate    (self, jd,          ttype=None)           : pass 
    #   jd:        saga.job.Description
    #   ttype:     saga.task.type enum
    #   ret:       None / saga.Task

    def signal     (self, signum,      ttype=None)           : pass 
    #   signum:    int
    #   ttype:     saga.task.type enum
    #   ret:       None / saga.Task


    description = property (get_description)  # Description
    stdin       = property (get_stdin)        # os.File
    stdout      = property (get_stdout)       # os.File
    stderr      = property (get_stderr)       # os.File


    #-----------------------------------------------------------------
    #
    # task methods flattened into job :-/
    #
    def run         (self)                         : pass 
    #   ret:        None

    def cancel      (self, timeout=None)           : pass 
    #   timeout:    float
    #   ret:        None

    def wait        (self, timeout=-1)             : pass 
    #   timeout:    float 
    #   ret:        None

    def get_state   (self)                         : pass 
    #   ret:        Task/Job state enum

    def get_result  (self)                         : pass 
    #   ret:        <result type>
    #   note:       this will always return None for a job.

    def get_object  (self)                         : pass 
    #   ret:        <object type>
    #   note:       this will return the job_service which created the job.

    def raise       (self)                         : pass 
    #   ret:        <exception type>
    #   note:       if job failed, that will re-raise an exception describing 
    #               why, if that exists.  Otherwise, the call does nothing.


    state     = property (get_state)       # state enum
    result    = property (get_result)      # result type    (None)
    object    = property (get_object)      # object type    (job_service)
    exception = property (get_exception)   # exception type



class Self (Job, monitoring.Steerable) :

    def __init__(self):
    
        # set attribute interface properties
        self.attributes_extensible_  (False)
        self.attributes_camelcasing_ (True)

    pass

